'''
This command will import orders from all ODS files in the specified directory.
'''
import os
from django.core.management.base import BaseCommand, CommandError
from pyexcel_ods import get_data

from orders.models import Order, OrderItem
from customers.models import Customer
from products.models import Product
from suppliers.models import Supplier


class Command(BaseCommand):
    help = 'Import orders from a CSV file'

    def add_arguments(self, parser):
        # Directory where the files are located
        parser.add_argument('directory', type=str, help='Directory where the files are located')

    def handle(self, *args, **options):
        directory = options['directory']

        if not os.path.isdir(directory):
            raise CommandError(f'The directory "{directory}" does not exist')

        # List all ODS files in the directory
        files = [f for f in os.listdir(directory) if f.endswith('.ods')]

        for file in files:
            data = self.load_sheet(os.path.join(directory, file))
            print(data[0])
            break


    def load_sheet(self, file_path):
        '''
        Load the sheet data into a list of dictionaries
        '''
        sheet_data = get_data(file_path)
        raw_data = sheet_data[list(sheet_data.keys())[0]]
        headers = raw_data[0]
        titles = raw_data[1:]

        # Convert the data to a list of dictionaries
        data = []
        for title in titles:
            data.append(dict(zip(headers, title)))

        return data
