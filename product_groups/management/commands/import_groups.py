'''
Import products from a ODS file
'''
import os
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from pyexcel_ods import get_data
from tqdm import tqdm

from product_groups.models import ProductGroup, ProductGroupItem
from products.models import Product, ProductCategory
from suppliers.models import Supplier


ROWS_TRANSLATIONS = [
    ('EDITORA', 'supplier'),
    ('CÓD. PANINI', 'supplier_internal_id'),
    ('CATEGORIA', 'category'),
    ('TÍTULO', 'title'),
    ('ISBN', 'sku'),
    ('LANÇAMENTO', 'release_date'),
    ('PREÇO R$', 'price'),
    ('SINOPSE', 'description'),
]


class Command(BaseCommand):
    '''
    Import products from a ODS file
    '''
    help = 'Import products from a ODS file'

    debug = False

    def add_arguments(self, parser):
        parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    def handle(self, *args, **options):
        # Load IMPORT_PATH from settings
        import_path = settings.IMPORT_PATH
        import_path = os.path.join(import_path, 'Grupos')

        if options['debug']:
            self.debug = True

        # Check if the import path exists
        if not os.path.isdir(import_path):
            raise CommandError(f'The import path "{import_path}" does not exist')

        # List all ODS files from the import path
        files = []
        for root, _, filenames in os.walk(import_path):
            for filename in filenames:
                if filename.endswith('.ods'):
                    files.append(os.path.join(root, filename))

        for filename in files:
            # Get the filename without the extension
            base_filename = os.path.basename(filename).split('.')[0]

            # Get the group
            group_name = base_filename.split(' - ')[1]
            group, _ = self.get_products_group(group_name)

            # Get the raw data from the file and convert it to a list of dictionaries
            raw_data = get_data(filename)
            products = self.get_products_data(raw_data)

            # If len of group items is the same as len of products
            # then the group is already imported
            if len(group.group_items.all()) == len(products):
                tqdm.write(f'Group "{group.name}" already imported')
                continue

            for product_data in tqdm(products, desc='Importing products'):
                product = self.try_to_get_product(product_data)

                if not product:
                    try:
                        product = self.import_product(product_data)
                    except CommandError as exc:
                        # Delete the group
                        group.delete()
                        raise exc

                if not product:
                    raise CommandError(f'Product not found: {product_data}')

                self.add_product_to_group(product, group)

            # Compare the total number of products in the group
            # with the number of products in the file
            group_products = ProductGroupItem.objects.filter(group=group).count()
            if group_products != len(products):
                raise CommandError(f'The total number of products in the group "{group_products}" '
                    f'"{group.name}" is different from the number '
                    f'of products in the file "{len(products)}"')

    def get_products_data(self, raw_data):
        '''
        Get the products data from the raw data
        '''
        # Get the first sheet
        sheet_data = list(raw_data.values())[0]

        # Identify the row with the headers
        header_row_number = 0
        for i, row in enumerate(sheet_data):
            if 'ISBN' in row:
                header_row_number = i
                break

        # Get the header row
        header_row = sheet_data[header_row_number]

        # Set all headers to uppercase
        header_row = [header.upper() for header in header_row]

        # Translate the headers
        for translation in ROWS_TRANSLATIONS:
            if translation[0] in header_row:
                header_row[header_row.index(translation[0])] = translation[1]

        # Get the products rows
        product_rows = sheet_data[header_row_number + 1:]
        products = [dict(zip(header_row, product_row)) for product_row in product_rows]

        # Remove empty rows
        products = [product for product in products if product]

        return products


    def get_products_group(self, group_name):
        '''
        Get the products group
        '''
        group, created = ProductGroup.objects.get_or_create(name=group_name)
        return group, created


    def get_supplier(self, supplier_name):
        '''
        Get the supplier
        '''
        supplier = Supplier.objects.get(short_name=supplier_name)
        return supplier


    def try_to_get_product(self, product_data):
        '''
        Try to get the product
        '''
        supplier = None
        if 'supplier' in product_data:
            supplier = self.get_supplier(product_data['supplier'])
        if not supplier:
            raise CommandError(f'Supplier not found: {product_data}')

        product = None

        has_valid_internal_id = 'supplier_internal_id' in product_data and \
            len(product_data['supplier_internal_id'].strip()) > 0

        if has_valid_internal_id:
            if self.debug:
                tqdm.write(f'Seeking with internal ID: {product_data["supplier_internal_id"]}')

            product = Product.objects.filter(
                supplier_internal_id=str(product_data['supplier_internal_id'].strip()),
                supplier=supplier
            ).first()

        # SKUs that don't start with 978 probably belong to series that contain
        # duplicated ISBNs, so another field - supplier_internal_id - should be used
        has_valid_sku = 'sku' in product_data and str(product_data['sku'])[:3] == '978' and \
            (isinstance(product_data['sku'], int) or product_data['sku'].isdigit())

        if not product and has_valid_sku:
            if self.debug:
                tqdm.write(f'Not found using internal ID. Seeking with SKU: {product_data["sku"]}')

            product = Product.objects.filter(
                sku=str(product_data['sku']).strip(),
                supplier=supplier
            ).first()


        no_valid_identifier = not has_valid_internal_id and not has_valid_sku

        if not product and 'title' in product_data and no_valid_identifier:
            if self.debug:
                tqdm.write('Not found using internal ID or SKU.'
                    f'Seeking with title: {product_data["title"]}')

            product = Product.objects.filter(
                name=product_data['title'].strip().upper(),
                supplier=supplier
            ).first()

        return product


    def import_product(self, product_data):
        '''
        Import a product
        '''
        supplier = None
        if 'supplier' in product_data:
            supplier = self.get_supplier(product_data['supplier'])
        if not supplier:
            raise CommandError(f'Supplier not found: {product_data}')

        try:
            release_date = product_data['release_date']
        except KeyError:
            release_date = None

        # If release_date is not None and it's a string, convert it to a date
        if release_date and isinstance(release_date, str):
            release_date = datetime.datetime.strptime(release_date, '%d/%m/%Y')

        if 'category' in product_data and len(product_data['category'].strip()) > 0:
            category, _ = ProductCategory.objects.get_or_create(
                name=product_data['category'].strip().upper()
            )
        else:
            category = None

        # Check if the price is present and if it's a string
        if product_data['price'] and isinstance(product_data['price'], str):
            # Remove trailing 'BRL' from the price
            try:
                product_data['price'] = float(product_data['price'].replace('BRL', '').replace(',', '.').strip())
            except ValueError as exc:
                raise CommandError(f'Invalid price format: {product_data["price"]} for product {product_data["title"]} - ISBN: {product_data["title"]}')

        sku = product_data['sku'] if 'sku' in product_data \
            and product_data['sku'] \
            and len(str(product_data['sku']).strip()) > 0 \
            and str(product_data['sku']).isdigit() else None

        supplier_internal_id = product_data['supplier_internal_id'].strip() \
            if 'supplier_internal_id' in product_data \
            and len(str(product_data['supplier_internal_id']).strip()) > 0 else None

        description = product_data['description'].strip() \
            if 'description' in product_data \
            and len(product_data['description'].strip()) > 0 else None,

        common_defaults = {
            'supplier': supplier,
            'release_date': release_date,
            'category': category,
            'price': product_data['price'],
            'description': description
        }

        if sku:
            product, created = Product.objects.get_or_create(
                name=product_data['title'].strip().upper(),
                sku=sku,
                defaults=common_defaults | {
                    'supplier_internal_id': supplier_internal_id
                }
            )
        elif supplier_internal_id:
            product, created = Product.objects.get_or_create(
                name=product_data['title'].strip().upper(),
                supplier_internal_id=supplier_internal_id,
                defaults=common_defaults | {
                    'sku': sku
                }
            )
        else:
            product, created = Product.objects.get_or_create(
                name=product_data['title'].strip().upper(),
                defaults=common_defaults | {
                    'sku': sku,
                    'supplier_internal_id': supplier_internal_id
                }
            )

        if self.debug:
            if created:
                tqdm.write(f'Product "{product.name}" created')
            else:
                tqdm.write(f'Product "{product.name}" already exists')

        return product


    def add_product_to_group(self, product, group):
        '''
        Add a product to a group
        '''
        # Check if the product is already in the group
        if ProductGroupItem.objects.filter(product=product, group=group).exists():
            self.delete_group(group)
            raise CommandError(f'Product "{product.name}" already exists in group "{group.name}"')

        product_group_item = ProductGroupItem.objects.create(
            product=product,
            group=group
        )

        if product_group_item and self.debug:
            tqdm.write(f'Product "{product.name}" added to group "{group.name}"')

    def delete_group(self, group):
        '''
        Delete a group
        '''
        for product_group_item in group.group_items.all():
            product_group_item.delete()
        group.delete()

        if self.debug:
            tqdm.write(f'Group "{group.name}" deleted')
