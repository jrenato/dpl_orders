import os
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from pyexcel_ods import get_data, save_data


class Command(BaseCommand):
    help = 'Reads an ods file, converts it into a list of dicts and print its contents'
    export_path = None

    def add_arguments(self, parser):
        parser.add_argument('export_path', type=str)

    def handle(self, *args, **options):
        import_path = settings.IMPORT_PATH
        import_path = os.path.join(import_path, 'Automático')

        self.export_path = options['export_path']

        preorders_result = {}

        for root, _, filenames in os.walk(import_path):
            for filename in filenames:
                # If file extension is not .ods, skip
                if not filename.endswith('.ods'):
                    continue

                # The filename has a format like 'automatico - %d-%m-%Y - %H-%M.ods'
                # Parse the datetime from the filename
                date_string_components = filename.split('.')[0].split(' - ')
                date_string = ' - '.join(date_string_components[1:])
                sheet_datetime = datetime.datetime.strptime(date_string, '%d-%m-%Y - %H-%M')

                preorders_data, customer_list = self.read_ods_file(os.path.join(root, filename))
                preorders = self.generate_preorders(preorders_data, customer_list)

                if sheet_datetime.date() in preorders_result:
                    preorders_result[sheet_datetime.date()][sheet_datetime.time()] = {
                        'preorders': preorders,
                    }
                else:
                    preorders_result[sheet_datetime.date()] = {
                        sheet_datetime.time(): {
                            'preorders': preorders,
                        }
                    }

        self.generate_sheets(preorders_result)


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

        # Generate a list of customers
        customer_list = self.get_customer_list(header_row)

        return products, customer_list


    def get_customer_list(self, list_of_columns):
        customer_list = list_of_columns.copy()
        customer_list.remove('DATA')
        customer_list.remove('ISBN')
        customer_list.remove('TÍTULO')
        customer_list.remove('TOTAL')

        return customer_list


    def generate_preorders(self, preorders_data, customer_list):
        preorders = {}

        for customer in customer_list:
            for product in preorders_data:
                if customer in product:
                    if not customer in preorders:
                        preorders[customer] = []

                    preorders[customer].append(
                        {
                            'isbn': product['ISBN'],
                            'title': product['TÍTULO'],
                            'qtd': product[customer],
                        }
                    )

        return preorders


    def generate_sheets(self, preorders):
        # Print all keys
        for preorders_date in preorders.keys():
            # Create a directory for the date in the export path, if it doesn't exist
            date_string = preorders_date.strftime('%Y-%m-%d')
            if not os.path.exists(os.path.join(self.export_path, date_string)):
                os.makedirs(os.path.join(self.export_path, date_string))
            for preorders_time in preorders[preorders_date].keys():
                time_string = preorders_time.strftime('%H-%M')
                # Create a directory for the time in the export path, if it doesn't exist
                if not os.path.exists(os.path.join(self.export_path, date_string, time_string)):
                    os.makedirs(os.path.join(self.export_path, date_string, time_string))
                # Generate the sheet
                # self.generate_sheet(date_string, time_string, preorders[preorders_date][preorders_time]['preorders'])


    # def generate_sheet(self, date_string, time_string, preorders):
    #     #TODO: Generate the sheet
    #     file_path = os.path.join(self.export_path, date_string, time_string, 'preorders.ods')
    #     data = OrderedDict() # from collections import OrderedDict
    #     data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
    #     data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
    #     save_data("your_file.ods", data)
