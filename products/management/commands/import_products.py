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


class Command(BaseCommand):
    '''
    Import products from a ODS file
    '''
    help = 'Import products from a ODS file'

    # def add_arguments(self, parser):
    #     parser.add_argument('file', type=str, help='File to import')
    #     parser.add_argument('--supplier', type=str, help='Supplier name')

    def handle(self, *args, **options):
        # Load IMPORT_PATH from settings
        import_path = settings.IMPORT_PATH
        import_path = os.path.join(import_path, 'Produtos')

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
                self.import_product(product_data, supplier, group)


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
        supplier, _ = Supplier.objects.get_or_create(
            short_name=supplier_name,
            defaults={
                'name': supplier_name,
            }
        )
        return supplier


    def import_product(self, product_data, supplier, group):
        '''
        Import a product
        '''

        try:
            release_date = product_data['Lançamento']
        except KeyError:
            print(product_data)
            raise CommandError('Lançamento não encontrado')

        # If release_date is not None and it's a string, convert it to a date
        if release_date and isinstance(release_date, str):
            release_date = datetime.datetime.strptime(release_date, '%d/%m/%Y')

        category, _ = ProductCategory.objects.get_or_create(
            name=product_data['Categoria'].strip().upper()
        )

        # Remove trailing 'BRL' from the price
        product_data['Preço R$'] = float(product_data['Preço R$'].replace('BRL', '').strip())

        product, _ = Product.objects.get_or_create(
            name=product_data['Título'].strip().upper(),
            sku=product_data['ISBN'],
            defaults={
                'supplier': supplier,
                'supplier_internal_id': product_data['Cód. Panini'],
                'release_date': release_date,
                'category': category,
                'price': product_data['Preço R$'],
                'description': product_data['Sinopse'].strip(),
            }
        )

        ProductGroupItem.objects.get_or_create(
            product=product,
            group=group
        )
