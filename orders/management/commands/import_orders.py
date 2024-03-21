'''
This command will import orders from a ODS file
'''
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from pyexcel_ods import get_data
from tqdm import tqdm

from orders.models import Order, OrderItem, ORDER_STATUS_CHOICES
from customers.models import Customer
from products.models import Product
from product_groups.models import ProductGroup


ROWS_TRANSLATIONS = [
    ('EDITORA', 'supplier'),
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
            tqdm.write(f'Importing orders from {os.path.basename(filename).split(".")[0]}')
            # Get the raw data from the file and convert it to a list of dictionaries
            raw_data = get_data(filename)
            orders_data = self.get_orders_data(raw_data)

            group_name = filename.split(os.sep)[-1].split('.')[0]
            product_group = ProductGroup.objects.get(name=group_name)

            if not product_group:
                raise CommandError(f'The product group "{group_name}" does not exist')

            for order_data in tqdm(orders_data, desc='Importing products orders'):
                self.import_order(order_data, product_group)


    def get_orders_data(self, raw_data):
        '''
        Get the orders data from the raw data
        '''
        sheet_data = list(raw_data.values())[0]
        header_row = sheet_data[0]

        # Rename the header row
        for translation in ROWS_TRANSLATIONS:
            if translation[0] in header_row:
                header_row[header_row.index(translation[0])] = translation[1]

        product_rows = sheet_data[1:]

        # Convert the product rows to a list of dictionaries
        products = [dict(zip(header_row, row)) for row in product_rows]

        # Remove empty rows
        products = [product for product in products if product]

        return products


    def import_order(self, order_data, product_group):
        '''
        Import an order
        '''
        # Order data without a valid product
        if not order_data['title'] and not order_data['sku']:
            return

        product = self.get_product(order_data)
        if not product:
            # A product should exist
            raise CommandError(f'Product not found: {order_data["sku"]} - {order_data["title"]}')

        keys_to_skip = [
            'supplier', 'supplier_internal_id', 'sku', 'title',
        ]

        # Iterate over the order data and create the order items
        for key, value in order_data.items():
            if not value:
                continue

            if key in keys_to_skip:
                continue

            # Get or create the customer
            customer = self.get_customer(key)

            # Get or create a pending order, using the customer
            # and product group as primary keys.
            order, _ = Order.objects.get_or_create(
                customer=customer,
                product_group=product_group,
                status='PE',
            )
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
        product = None

        has_valid_internal_id = 'supplier_internal_id' in order_data and \
            len(order_data['supplier_internal_id'].strip()) > 0

        if has_valid_internal_id:
            product = Product.objects.filter(
                supplier_internal_id=str(order_data['supplier_internal_id'].strip()),
            ).first()

        # SKUs that don't start with 978 probably belong to series that contain
        # duplicated ISBNs, so another field - supplier_internal_id - should be used
        has_valid_sku = 'sku' in order_data and str(order_data['sku'])[:3] == '978' and \
            (isinstance(order_data['sku'], int) or order_data['sku'].isdigit())

        if has_valid_sku:
            product = Product.objects.filter(
                sku=str(order_data['sku']).strip(),
            ).first()

        no_valid_identifier = not has_valid_internal_id and not has_valid_sku

        if not product and 'title' in order_data and no_valid_identifier:
            product = Product.objects.filter(
                name=order_data['title'].strip().upper(),
            ).first()

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
