'''
Management command to import product groups from ODS files in a directory
'''
import os

from django.core.management.base import BaseCommand, CommandError

from pyexcel_ods import get_data

from product_groups.models import ProductGroup
from products.models import Product, ProductCategory
from suppliers.models import Supplier
from customers.models import Customer


class Command(BaseCommand):
    '''
    Import product groups from ODS files in a directory
    '''
    help = "Imports product groups from ODS files in a directory"

    def add_arguments(self, parser):
        parser.add_argument("files_dir", type=str)

    def handle(self, *args, **options):
        files_dir = options["files_dir"]

        # List all ODS files in the directory
        self.stdout.write(f"Looking for ODS files in {files_dir}")
        ods_files = []
        for file in os.listdir(files_dir):
            if file.endswith(".ods"):
                file_path = os.path.join(files_dir, file)
                ods_files.append(file_path)

        if not ods_files:
            raise CommandError("No ODS files found in the directory")

        key_count = 0

        for ods_file in ods_files:
            group_products = self.load_ods_file(ods_file)
            self.save_product_group(ods_file.split('/')[-1].split('.')[0], group_products)

        self.stdout.write(self.style.SUCCESS('Success'))

    def load_ods_file(self, file_path):
        '''
        Load an ODS file and convert it to a list of dictionaries
        '''
        data = get_data(file_path)
        # Get first key from the dictionary
        sheet_name = list(data.keys())[0]
        sheet = data[sheet_name]

        # Get the header row
        header = sheet[0]

        # Get the data rows
        rows = sheet[1:]

        # Convert the data to a list of dictionaries
        data = []
        for row in rows:
            item = {}
            for index, value in enumerate(row):
                try:
                    item[header[index]] = value
                except IndexError as exc:
                    self.stdout.write(self.style.ERROR(f"Error for value: {value}"))
                    self.stdout.write(self.style.ERROR(f"Error for index: {index}"))
                    self.stdout.write(self.style.ERROR(f"In ODS file: {file_path.split('/')[-1]}"))
                    raise exc

            data.append(item)

        return data

    def save_product_group(self, group_name, group_products):
        print(f'Saving product group {group_name} with {len(group_products)-1} products')

        product_group, _ = ProductGroup.objects.get_or_create(name=group_name)

        for group_product in group_products:
            # Check if group_product has a key 'la' and if is not empty
            if 'la' in group_product and group_product['la']:
                supplier, _ = Supplier.objects.get_or_create(name=group_product['la'])
            if 'Genero' in group_product and group_product['Genero']:
                category, _ = ProductCategory.objects.get_or_create(name=group_product['Genero'])
