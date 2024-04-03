'''
Command to sync data with metabooks
'''
import os
import datetime
import requests
import json
from PIL import Image
from io import BytesIO

from django.core.management.base import BaseCommand
from django.conf import settings

from tqdm import tqdm

from metabooks.models import MetabooksSync
from suppliers.models import Supplier
from products.models import Product, ProductImage


class Command(BaseCommand):
    '''
    Command to sync data with metabooks
    '''
    help = 'Syncs data with metabooks'
    mb_url = settings.MB_URL
    mb_username = settings.MB_USERNAME
    mb_password = settings.MB_PASSWORD
    media_root = settings.MEDIA_ROOT

    timeout = 5
    max_results = 50
    debug = False
    force = False

    upload_to_path = os.path.join(media_root, 'products', 'images')


    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true', help='Reset pending syncs')
        parser.add_argument('--debug', action='store_true', help='Debug mode')
        parser.add_argument('--force', action='store_true', help='Force details update')


    def handle(self, *args, **options):
        self.force = options['force']

        self.debug = options['debug']
        if self.debug:
            self.stdout.write(self.style.WARNING('Debug mode is on'))

        if options['reset']:
            for mb_sync in MetabooksSync.objects.filter(concluded=False):
                if not mb_sync.bearer or self.logout(mb_sync):
                    mb_sync.concluded = True
                    mb_sync.save()

        for supplier in tqdm(Supplier.objects.filter(mb_id__isnull=False), desc='Suppliers'):
            try:
                mb_sync = MetabooksSync.objects.get(concluded=False, supplier=supplier)
            except MetabooksSync.DoesNotExist:
                mb_sync = MetabooksSync.objects.create(supplier=supplier)

            if not mb_sync.bearer:
                if self.debug:
                    self.stdout.write(self.style.WARNING('Bearer token not found'))
                self.login(mb_sync)

            if mb_sync.current_page <= mb_sync.last_page and not mb_sync.concluded:
                tqdm.write('Parsing first page')
                self.parse_current_page(mb_sync)

            if not mb_sync.concluded:
                for _ in tqdm(
                    range(mb_sync.current_page, mb_sync.last_page),
                    desc='Parsing pages', leave=False
                ):
                    self.parse_current_page(mb_sync)

        mb_sync.logout()
        mb_sync.concluded = True
        mb_sync.save()


    def login(self, mb_sync):
        '''
        Login to the metabooks API
        '''
        data = {
            'username': self.mb_username,
            'password': self.mb_password
        }
        response = requests.post(f'{self.mb_url}/login', json=data, timeout=self.timeout)

        if response.status_code == 200:
            if self.debug:
                self.stdout.write(self.style.SUCCESS(
                    f'Login successful with message {response.text}')
                )
            else:
                self.stdout.write(self.style.SUCCESS('Login successful'))

            mb_sync.bearer = response.text
            mb_sync.save()
            return True
        else:
            if self.debug:
                self.stdout.write(self.style.ERROR(
                    f'Login failed with status code \
                        {response.status_code} and message {response.text}')
                )
            else:
                self.stdout.write(self.style.ERROR('Login failed'))
            return False


    def logout(self, mb_sync):
        '''
        Logout from the metabooks API
        '''
        headers = {'Authorization': f'Bearer {mb_sync.bearer}'}
        response = requests.get(f'{self.mb_url}/logout', headers=headers, timeout=self.timeout)

        if response.status_code == 200:
            # Logout successful
            self.stdout.write(self.style.SUCCESS('Logout successful'))
        else:
            # Logout failed
            self.stdout.write(self.style.ERROR('Logout failed'))

        return True


    def parse_current_page(self, mb_sync):
        '''
        Parse the current page
        '''
        headers = {'Authorization': f'Bearer {mb_sync.bearer}'}

        url = f'{self.mb_url}/products?search=VL={mb_sync.supplier.mb_id}'
        url += f'&page={mb_sync.current_page}&size={self.max_results}'
        url += '&sort=modificationDate&direction=desc'

        response = requests.get(url, headers=headers, timeout=self.timeout)

        if response.status_code == 200:
            # Compare mb_sync.last_page with response.json()['totalPages']
            if mb_sync.last_page != response.json()['totalPages']:
                mb_sync.last_page = response.json()['totalPages']
                mb_sync.save()
            # Parse the current page
            self.parse_products(response.json()['content'], mb_sync)
        else:
            # Error parsing the current page
            self.stdout.write(self.style.ERROR(
                f'Error parsing the current page with status code \
                    {response.status_code} and message {response.text}')
            )

        mb_sync.current_page += 1
        if mb_sync.current_page > mb_sync.last_page:
            mb_sync.concluded = True
            mb_sync.save()


    def parse_products(self, products_data, mb_sync):
        '''
        Parse the products
        '''
        for product_data in tqdm(products_data, desc='Parsing Products', leave=False):
            if self.debug:
                self.stdout.write(self.style.SUCCESS(f'Parsing product {product_data["id"]}'))

            # Only parse products with the expected product type
            # pbook = published book
            # ebook = e-book
            if product_data['productType'] == 'pbook':
                self.parse_product(product_data, mb_sync)


    def parse_product(self, product_data, mb_sync):
        '''
        Parse the product
        '''
        # Evaluate the len of publication date and update the release date
        if len(product_data['publicationDate']) == 10:
            # It's the expected format, just use it
            pass
        elif len(product_data['publicationDate']) == 4:
            # It's an year, just set it as the first day of the year
            product_data['publicationDate'] = f'01/01/{product_data["publicationDate"]}'
        else:
            raise ValueError(f'Invalid publicationDate format: {product_data["publicationDate"]} '
                f'for product {product_data["title"]} - ISBN: {product_data["gtin"]}')

        try:
            release_date = datetime.datetime.strptime(
                product_data['publicationDate'], '%d/%m/%Y'
            ).date() if product_data['publicationDate'] else None
        except ValueError as exc:
            raise ValueError('Invalid date format: '
                f'{product_data["publicationDate"]} for product {product_data["title"]} - '
                f'ISBN: {product_data["gtin"]}') from exc

        mb_create_date = datetime.datetime.strptime(
            product_data['createDate'], '%d/%m/%Y'
        ).date() if product_data['createDate'] else None

        mb_updated_date = datetime.datetime.strptime(
            product_data['lastModifiedDate'], '%d/%m/%Y'
        ).date() if product_data['lastModifiedDate'] else None

        product, created = Product.objects.get_or_create(
            mb_id=product_data['id'],
            defaults={
                'supplier': mb_sync.supplier,
                'name': product_data['title'].strip().upper(),
                'sku': product_data['gtin'],
                'price': product_data['priceBrl'],
                'mb_price': product_data['priceBrl'],
                'release_date': release_date,
                'supplier_internal_id': product_data['ordernumber'],
                'description': product_data['mainDescription'],
                'mb_created': mb_create_date,
                'mb_updated': mb_updated_date
            }
        )

        should_get_details = False
        updated = False

        if created:
            should_get_details = True

        if product.mb_updated != mb_updated_date:
            # TODO: Replace this with the implementation of parse_product_details
            #product.update(
            product.supplier = mb_sync.supplier
            product.name = product_data['title'].strip().upper()
            product.sku = product_data['gtin']
            # product.price = product_data['priceBrl']
            product.mb_price = product_data['priceBrl']
            product.release_date = release_date
            product.supplier_internal_id = product_data['ordernumber']
            product.description = product_data['mainDescription']
            # product.mb_created = mb_create_date
            product.mb_updated = mb_updated_date

            product.save()

            should_get_details = True
            updated = True

        if self.debug:
            if created:
                tqdm.write(f'Product {product.name} created')
            elif updated:
                tqdm.write(f'Product {product.name} updated')

        if should_get_details or self.force:
            # self.get_product_details(mb_sync, product)
            self.get_product_cover(mb_sync, product)


    def get_product_details(self, mb_sync, product):
        '''
        Get the product details
        '''
        headers = {'Authorization': f'Bearer {mb_sync.bearer}'}
        url = f'{self.mb_url}/product/{product.mb_id}'
        response = requests.get(url, headers=headers, timeout=self.timeout)

        if response.status_code == 200:
            # TODO: Parse the product details
            product_data = response.json()


    def get_product_cover(self, mb_sync, product):
        '''
        Get the product cover as image/jpeg and store it as a ProductImage
        '''
        size = 'l' # Possible values: l, m, s

        headers = {
            'Authorization': f'Bearer {mb_sync.bearer}',
            'Content-Type': 'image/jpeg',
        }

        # # Check if FRONTCOVER is available
        # url = f'{self.mb_url}//asset/mmo/{product.id}'
        # response = requests.get(url, headers=headers, timeout=self.timeout)

        # # product_has_frontcover = False
        # if response.status_code == 200:
        #     for product_media in response.json():
        #         if product_media['type'] == 'FRONTCOVER':
        #             product_has_frontcover = True
        # else:
        #     # Error checking if FRONTCOVER is available
        #     self.stdout.write(self.style.ERROR(
        #         f'Error checking if FRONTCOVER is available with status code \
        #             {response.status_code} and message {response.text} for product {product.name}')
        #     )

        # # If product does not have a frontcover, return
        # if not product_has_frontcover:
        #     return

        url = f'{self.mb_url}/cover/{product.sku}/{size}'
        response = requests.get(url, headers=headers, timeout=self.timeout)

        if response.status_code == 200:
            # Delete old cover images
            for product_image in ProductImage.objects.filter(product=product, is_main=True):
                # TODO: Fix error when deleting old cover images
                # try:
                #     os.remove(os.path.join(settings.MEDIA_ROOT, product_image.image.url))
                # except FileNotFoundError:
                #     tqdm.write(f'File not found: {product_image.image.url}')
                product_image.delete()

            # Save response.content as a ProductImage
            img_buffer = BytesIO()
            img_buffer.write(response.content)
            img = Image.open(img_buffer)
            img_file_path = os.path.join(self.upload_to_path, f'{product.sku}.jpg')

            # To prevent errors, convert to RGB
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            img.save(img_file_path, format='JPEG')

            # Create new cover image
            product_image = ProductImage.objects.create(
                product=product,
                image=os.path.join('products', 'images', f'{product.sku}.jpg'),
                is_main=True
            )
            # product_image.image.save(
            #     f'{product.sku}.jpg',
            #     ContentFile(response.content),
            #     save=True
            # )
        else:
            if response.status_code in [404, 503]:
                response_data = json.loads(response.json())
                try:
                    if 'error' in response_data and response_data['error'] == 'not_found':
                        tqdm.write(f'Error getting the product cover for product {product.name}')
                        return
                    else:
                        raise requests.HTTPError(f'Error {response.status_code} getting the product '
                            f'cover for product {product.name} - {response.text} {type(response_data)}')
                except TypeError:
                    # raise an exception with response_data and what type it is
                    raise Exception(f'Wrong type for response data, should be a dict {type(response_data)}')
            else:
                raise requests.HTTPError(f'Error {response.status_code} getting the product '
                    f'cover for product {product.name} - {response.text} ')
