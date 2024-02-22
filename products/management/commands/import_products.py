'''
Import products from a ODS file
'''
import os
import datetime

from django.core.management.base import BaseCommand, CommandError

from pyexcel_ods import get_data
from tqdm import tqdm

from products.models import Product, ProductGroup, ProductGroupItem
from suppliers.models import Supplier


class Command(BaseCommand):
    '''
    Import products from a ODS file
    '''
    help = 'Import products from a ODS file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='File to import')
        parser.add_argument('--supplier', type=str, help='Supplier name')

    def handle(self, *args, **options):
        file = options['file']

        if not os.path.isfile(file):
            raise CommandError(f'The file "{file}" does not exist')

        raw_data = get_data(file)
        products = self.get_products_data(raw_data)

        # Get the file name without the extension and create the group
        file_name = os.path.basename(file).split('.')[0]
        group = self.get_products_group(file_name)

        if not options['supplier'] and 'EDITORA' not in products[0]:
            raise CommandError('The supplier name is required')

        supplier = self.get_supplier(options['supplier'])

        for product_data in tqdm(products, desc='Importing products'):
            self.import_product(product_data, supplier, group)


    def get_products_data(self, raw_data):
        '''
        Get the products data from the raw data
        '''
        sheet_data = list(raw_data.values())[0]
        sheet_data = sheet_data[1:]
        products = [dict(zip(sheet_data[0], row)) for row in sheet_data[1:]]

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
        supplier, _ = Supplier.objects.get_or_create(name=supplier_name)
        return supplier


    def import_product(self, product_data, supplier, group):
        '''
        Import a product
        '''

        release_date = product_data['Lançamento']
        # If release_date is not None and it's a string, convert it to a date
        if release_date and isinstance(release_date, str):
            release_date = datetime.datetime.strptime(release_date, '%d/%m/%Y')

        product, _ = Product.objects.get_or_create(
            name=product_data['Título'].strip().upper(),
            sku=product_data['ISBN'],
            defaults={
                'supplier': supplier,
                'release_date': release_date,
                'description': product_data['Sinopse'],
                'price': product_data['Preço R$'],
                'supplier_internal_id': product_data['Cód. Panini'],
            }
        )

        ProductGroupItem.objects.get_or_create(
            product=product,
            group=group
        )
