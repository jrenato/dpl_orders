'''
Import products from a ODS file
'''
import os
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from pyexcel_ods import get_data
from tqdm import tqdm

from products.models import Product, ProductCategory, ProductGroup, ProductGroupItem
from suppliers.models import Supplier


ROWS_TRANSLATIONS = [
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

            # Get the supplier and the group
            supplier_name = base_filename.split(' - ')[0]
            supplier = self.get_supplier(supplier_name)
            group = self.get_products_group(base_filename)

            # Get the raw data from the file and convert it to a list of dictionaries
            raw_data = get_data(filename)
            products = self.get_products_data(raw_data)

            for product_data in tqdm(products, desc='Importing products'):
                product = self.try_to_get_product(product_data, supplier)

                has_identifier = str(product_data['sku']).isdigit() or \
                    len(str(product_data['supplier_internal_id'])) > 0

                if not product or has_identifier:
                    product = self.import_product(product_data, supplier)
                else:
                    raise CommandError(f'Product not found: {product_data}')

                if product:
                    self.add_product_to_group(product, group)


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
        group, _ = ProductGroup.objects.get_or_create(name=group_name)
        return group


    def get_supplier(self, supplier_name):
        '''
        Get the supplier
        '''
        supplier = Supplier.objects.get(short_name=supplier_name)
        return supplier


    def try_to_get_product(self, product_data, supplier):
        '''
        Try to get the product
        '''
        product = None

        # Note:
        # SKUs that don't start with 978 probably belong to series that contain
        # duplicated ISBNs, so another field - supplier_internal_id - should be used
        has_valid_sku = 'sku' in product_data and str(product_data['sku'])[:3] == '978' and \
            (isinstance(product_data['sku'], int) or product_data['sku'].isdigit())

        if has_valid_sku:
            if self.debug:
                tqdm.write(f'Seeking with SKU: {product_data["sku"]}')

            product = Product.objects.filter(
                sku=product_data['sku'],
                supplier=supplier
            ).first()

        if not product and 'supplier_internal_id' in product_data:
            if self.debug:
                tqdm.write(f'Seeking with internal ID: {product_data["supplier_internal_id"]}')

            product = Product.objects.filter(
                supplier_internal_id=product_data['supplier_internal_id'],
                supplier=supplier
            ).first()

        if not product and 'title' in product_data:
            if self.debug:
                tqdm.write(f'Seeking with title: {product_data["title"]}')

            product = Product.objects.filter(
                name=product_data['title'].strip().upper(),
                supplier=supplier
            ).first()

        return product


    def import_product(self, product_data, supplier):
        '''
        Import a product
        '''

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
            product_data['price'] = float(product_data['price'].replace('BRL', '').strip())

        supplier_internal_id = product_data['supplier_internal_id'].strip() \
            if 'supplier_internal_id' in product_data \
            and len(str(product_data['supplier_internal_id']).strip()) > 0 else None

        description = product_data['description'].strip() \
            if 'description' in product_data \
            and len(product_data['description'].strip()) > 0 else None,

        product, _ = Product.objects.get_or_create(
            name=product_data['title'].strip().upper(),
            sku=product_data['sku'],
            defaults={
                'supplier': supplier,
                'supplier_internal_id': supplier_internal_id,
                'release_date': release_date,
                'category': category,
                'price': product_data['price'],
                'description': description
            }
        )

        return product


    def add_product_to_group(self, product, group):
        '''
        Add a product to a group
        '''
        ProductGroupItem.objects.get_or_create(
            product=product,
            group=group
        )
