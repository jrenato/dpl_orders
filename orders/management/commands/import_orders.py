'''
This command will import orders from all ODS files in the specified directory.
'''
import os
from django.core.management.base import BaseCommand, CommandError

from pyexcel_ods import get_data
from tqdm import tqdm

from orders.models import Order, OrderItem
from customers.models import Customer
from products.models import Product, ProductCategory, ProductReleaseDateHistory,\
    ProductGroup, ProductGroupItem
from suppliers.models import Supplier


class Command(BaseCommand):
    '''
    Import orders from ODS files
    '''
    help = 'Import orders from ODS files'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Directory where the files are located')
        parser.add_argument(
            '--reset', action='store_true', help='Reset the database before importing the data'
        )

    def handle(self, *args, **options):
        directory = options['directory']

        if options['reset']:
            self.reset_database()

        if not os.path.isdir(directory):
            raise CommandError(f'The directory "{directory}" does not exist')

        # List all ODS files in the directory
        files = [f for f in os.listdir(directory) if f.endswith('.ods')]

        for file in tqdm(files, desc='Importing sheets'):
            data = self.load_sheet(os.path.join(directory, file))
            self.process_group(data, group_name=file.split('.')[0])


    def reset_database(self):
        '''
        Reset the database
        '''
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        ProductGroupItem.objects.all().delete()
        ProductGroup.objects.all().delete()
        Product.objects.all().delete()
        ProductReleaseDateHistory.objects.all().delete()
        ProductCategory.objects.all().delete()
        Supplier.objects.all().delete()
        Customer.objects.all().delete()


    def load_sheet(self, file_path):
        '''
        Load the sheet data into a list of dictionaries
        '''
        sheet_data = get_data(file_path)
        raw_data = sheet_data[list(sheet_data.keys())[0]]
        headers = raw_data[0]
        items = raw_data[1:]

        # Convert the data to a list of dictionaries
        data = []
        for item in items:
            data.append(dict(zip(headers, item)))

        return data


    def process_group(self, data, group_name):
        '''
        Process the data and create the orders
        '''
        tqdm.write(f'Processing group "{group_name}"')

        product_group, _ = ProductGroup.objects.get_or_create(name=group_name)

        for item in tqdm(data, desc='Processing items', leave=False):
            if not item:
                continue
            supplier = self.get_supplier(item)
            product = self.get_product(item, supplier)

            if not product:
                raise CommandError(f'Missing product data in {item} - group {group_name}')

            # Add the product to the group
            ProductGroupItem.objects.get_or_create(product=product, group=product_group)


    def get_supplier(self, data):
        '''
        Get the supplier by name, or create a new one if it doesn't exist
        '''
        if 'la' not in data or not data['la']:
            return None

        supplier, _ = Supplier.objects.get_or_create(name=data['la'])
        return supplier


    def get_product(self, data, supplier):
        '''
        Get the product by name, or create a new one if it doesn't exist
        '''
        if 'HQ' not in data or not data['HQ']:
            return None

        isbn = None
        if 'ISBN' in data and data['ISBN']:
            isbn = data['ISBN']

        category = None
        if 'Genero' in data and data['Genero']:
            category, _ = ProductCategory.objects.get_or_create(name=data['Genero'])

        release_date = None
        previous_date = None
        if 'Data' in data and data['Data']:
            release_date = data['Data']
            if 'Data atualizada' in data and data['Data atualizada']:
                release_date = data['Data atualizada']
                previous_date = data['Data']
        elif 'Data atualizada' in data and data['Data atualizada']:
            release_date = data['Data atualizada']

        if release_date:
            try:
                release_date = release_date.strftime('%Y-%m-%d')
            except AttributeError:
                release_date = None

        if previous_date:
            try:
                previous_date = previous_date.strftime('%Y-%m-%d')
            except AttributeError:
                previous_date = None

        product, _ = Product.objects.get_or_create(
            name=data['HQ'], defaults={
                'sku': isbn,
                'supplier': supplier,
                'category': category,
                'release_date': release_date,
            }
        )

        if previous_date:
            ProductReleaseDateHistory.objects.create(
                product=product, release_date=previous_date,
            )

        return product

# "la", "Data", "Data atualizada", "Genero", "ISBN", "HQ", "DATA DO PEDIDO", "PEDIDO", "OV",
# "NOTA FISCAL", "DATA DA ENTRADA", "Entrega automática / TIPO DA CAPA", "Automático",
# "TOTAL", "NOVA QUANTIA"
