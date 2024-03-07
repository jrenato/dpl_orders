'''
Command to sync data with metabooks
'''
import requests
import datetime

from django.core.management.base import BaseCommand
from django.conf import settings

from tqdm import tqdm

from metabooks.models import MetabooksSync
from suppliers.models import Supplier
from products.models import Product, ProductMBCategory


class Command(BaseCommand):
    '''
    Command to sync data with metabooks
    '''
    help = 'Syncs data with metabooks'
    mb_url = settings.MB_URL
    mb_username = settings.MB_USERNAME
    mb_password = settings.MB_PASSWORD
    timeout = 5
    max_results = 50
    debug = False


    def add_arguments(self, parser):
        parser.add_argument(
            '--reset', action='store_true',
            help='Reset all pending metabooks syncs'
        )
        parser.add_argument('--debug', action='store_true', help='Debug mode')


    def handle(self, *args, **options):
        self.debug = options['debug']
        # Message about debug mode
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
            return True
        else:
            # Logout failed
            self.stdout.write(self.style.ERROR('Logout failed'))
            return False


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
            # Parse the product
            self.parse_product(product_data, mb_sync)


    def parse_product(self, product_data, mb_sync):
        '''
        Parse the product
        '''
        release_date = datetime.datetime.strptime(
            product_data['publicationDate'], '%d/%m/%Y'
        ).date() if product_data['publicationDate'] else None

        product, _ = Product.objects.update_or_create(
            mb_id=product_data['id'],
            defaults={
                'supplier': mb_sync.supplier,
                'name': product_data['title'].strip().upper(),
                'description': product_data['mainDescription'],
                'price': product_data['priceBrl'],
                'sku': product_data['gtin'],
                'release_date': release_date,
                'supplier_internal_id': product_data['ordernumber'],
            }
        )

        # If the product has any mb_category, remove them
        # In that way, we can add the new ones, in case the product has changed
        product.mb_categories.clear()

        # Add the mb_categories to the product
        for thema_code in product_data['themaSubjects']:
            mb_category, _ = ProductMBCategory.objects.get_or_create(code=thema_code)
            product.mb_categories.add(mb_category)

        # TODO: Instead of this, just get the product details for all products
        for mb_category in product.mb_categories.all():
            if not mb_category.name or mb_category.name.strip() == '':
                self.get_product_details(mb_sync, product, mb_category)


    def get_product_details(self, mb_sync, product, mb_category):
        '''
        Get the product details
        '''
        headers = {'Authorization': f'Bearer {mb_sync.bearer}'}
        url = f'{self.mb_url}/product/{product.mb_id}'
        response = requests.get(url, headers=headers, timeout=self.timeout)

        if response.status_code == 200:
            # TODO: Parse the product details
            for subject in response.json()['subjects']:
                if 'subjectCode' not in subject:
                    self.stdout.write(self.style.ERROR(
                        f'Error parsing the product details for product {product.mb_id}')
                    )
                    raise ValueError('Error parsing the product details')

                if mb_category.code == subject['subjectCode']:
                    mb_category.name = subject['subjectHeadingText']
                    mb_category.save()
