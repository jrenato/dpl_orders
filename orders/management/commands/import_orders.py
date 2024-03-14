'''
This command will import orders from a ODS file
'''
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from pyexcel_ods import get_data
from tqdm import tqdm

from orders.models import Order, OrderItem
from customers.models import Customer
from products.models import Product


class Command(BaseCommand):
    '''
    Import orders from a ODS file
    '''
    help = 'Import orders from a ODS file'

    # def add_arguments(self, parser):
    #     parser.add_argument('file', type=str, help='File to import')


    def handle(self, *args, **options):
        # Load IMPORT_PATH from settings
        import_path = settings.IMPORT_PATH
        import_path = os.path.join(import_path, 'Pedidos')

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
            # Get the raw data from the file and convert it to a list of dictionaries
            raw_data = get_data(filename)
            products = self.get_products_data(raw_data)

            for product_data in tqdm(products, desc='Importing products orders'):
                self.import_order(product_data)


    def get_products_data(self, raw_data):
        '''
        Get the products data from the raw data
        '''
        sheet_data = list(raw_data.values())[0]
        products = [dict(zip(sheet_data[0], row)) for row in sheet_data[1:]]

        # Remove empty rows
        products = [product for product in products if product]

        return products


    def import_order(self, order_data):
        '''
        Import an order
        '''
        # Order data without a valid product
        if not order_data['TITULO'] and not order_data['ISBN']:
            return

        product = self.get_product(order_data)
        if not product:
            # A product should exist
            raise CommandError(f'Product not found: {order_data["ISBN"]} - {order_data["TITULO"]}')

        keys_to_skip = [
            "Data", "Data atualizada", "Genero", "ISBN",
            "TITULO", "TOTAL",	"DPL", "NOVA QUANTIA"
        ]

        # Iterate over the order data and create the order items
        for key, value in order_data.items():
            if not value:
                continue

            if key in keys_to_skip:
                continue

            # Get the customer, the customer is the key of the order data
            customer = self.get_customer(key)
            order, _ = Order.objects.get_or_create(customer=customer)
            order_item, created = OrderItem.objects.get_or_create(
                order=order, product=product, defaults={
                    'quantity': value,
                    'price': product.price,
                }
            )

            # If the order item already exists, update the quantity if necessary
            if not created and order_item.quantity != value:
                order_item.quantity = value
                order_item.save()


    def get_product(self, order_data):
        '''
        Get the product
        '''
        # Some suppliers don't provide have a unique SKU for each product
        # so we need to consider the product name as well
        try:
            product = Product.objects.get(sku=order_data['ISBN'], name=order_data['TITULO'].upper())
        except Product.DoesNotExist:
            return None

        return product


    def get_customer(self, customer_name):
        '''
        Get the customer
        '''
        customer, _ = Customer.objects.get_or_create(
            sheet_label=customer_name.strip().upper(),
            defaults={
                'name': customer_name.strip().upper(),
                'short_name': customer_name.strip().upper(),
            }
        )
        return customer
