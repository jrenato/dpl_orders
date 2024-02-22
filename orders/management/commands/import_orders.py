'''
This command will import orders from a ODS file
'''
import os
from django.core.management.base import BaseCommand, CommandError

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


    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='File to import')


    def handle(self, *args, **options):
        file = options['file']
        if not os.path.isfile(file):
            raise CommandError(f'The file "{file}" does not exist')

        # Get the raw data from the file and convert it to a list of dictionaries
        raw_data = get_data(file)
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
        product = self.get_product(order_data)
        if not product:
            #raise CommandError(f'Product not found: {order_data["ISBN"]} - {order_data["TITULO"]}')
            return

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
                order=order, product=product, defaults={'quantity': value}
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
        customer, _ = Customer.objects.get_or_create(name=customer_name.strip().upper())
        return customer
