import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from pyexcel_ods import get_data


class Command(BaseCommand):
    help = 'Reads an ods file, converts it into a list of dicts and print its contents'

    def handle(self, *args, **options):
        import_path = settings.IMPORT_PATH
        import_path = os.path.join(import_path, 'Automático')

        # Print all the files present in import_path
        for root, _, filenames in os.walk(import_path):
            for filename in filenames:
                preorders_data, customer_list = self.read_ods_file(os.path.join(root, filename))
                print(customer_list)

    def read_ods_file(self, filename):
        raw_data = get_data(filename)

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

        # Get the products rows
        product_rows = sheet_data[header_row_number + 1:]
        products = [dict(zip(header_row, product_row)) for product_row in product_rows]

        # Generate a customer list by making a copy of the header row and excluding DATA, ISBN, TÍTULO and TOTAL
        customer_list = header_row.copy()
        customer_list.remove('DATA')
        customer_list.remove('ISBN')
        customer_list.remove('TÍTULO')
        customer_list.remove('TOTAL')

        return products, customer_list
