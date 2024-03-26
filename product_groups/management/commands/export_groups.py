'''
Export groups to excel files
'''
import os

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.translation import gettext as _
from django.utils import dates

from openpyxl import load_workbook
from openpyxl.styles import Border, Alignment, Side, PatternFill
from tqdm import tqdm

from product_groups.models import ProductGroup


class Command(BaseCommand):
    '''
    Export groups to excel files
    '''
    help = 'Export groups to excel files'

    debug = False
    template_file = None
    align_center = Alignment(horizontal='center', vertical='center')
    border = Border(
        left=Side(border_style='thin'), right=Side(border_style='thin'),
        top=Side(border_style='thin'), bottom=Side(border_style='thin')
    )
    fill = PatternFill(fill_type='solid', start_color='00DEE6EF')

    def add_arguments(self, parser):
        parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    def handle(self, *args, **options):
        # Set the export path
        newsletters_path = os.path.join(settings.EXPORT_PATH, _('Newsletters Sheets'))
        if not os.path.isdir(newsletters_path):
            os.makedirs(newsletters_path)

        # Check if the export path exists
        if not os.path.isdir(newsletters_path):
            raise CommandError(f'The export path "{newsletters_path}" does not exist')

        # Set the template file
        self.template_file = os.path.join(
            settings.DOCUMENT_TEMPLATES_PATH, 'product_group_template.xltx'
        )

        if options['debug']:
            self.debug = True

        produt_groups = self.get_pending_product_groups()

        for product_group in tqdm(produt_groups, desc='Exporting groups'):
            self.export_product_group(product_group, newsletters_path)


    def get_pending_product_groups(self):
        '''
        Get the product groups with status 'PE'
        '''
        return ProductGroup.objects.filter(status='PE')


    def export_product_group(self, product_group, export_path):
        '''
        Export the product group to excel
        '''

        # Check for subdir named year/month_name in export path
        month_name = dates.MONTHS[product_group.created.month]
        subdir = os.path.join(export_path, product_group.created.strftime(f'%Y/{month_name}'))
        if not os.path.isdir(subdir):
            os.makedirs(subdir)

        # Create the excel file
        wb = load_workbook(self.template_file)
        wb.template = False
        ws = wb['Template']

        ws['A1'].value = product_group.name
        if product_group.customer_limit_date:
            ws['A9'].value = 'Data limite para pedido: ' \
                f'{product_group.customer_limit_date.strftime("%d/%m/%Y")}'

        line = 11

        for item in tqdm(product_group.group_items.all(), desc='Exporting items', leave=False):
            # Set values
            ws[f'A{line}'].value = item.product.supplier.short_name
            ws[f'B{line}'].value = item.product.release_date
            ws[f'C{line}'].value = item.product.sku
            ws[f'D{line}'].value = item.product.name
            ws[f'E{line}'].value = item.product.price
            ws[f'F{line}'].value = None

            # Set formats
            ws[f'B{line}'].number_format = 'dd/mm/yyyy'
            ws[f'E{line}'].number_format = '[$R$-416] #,##0.00;[$R$-416] #,##0.00-'
            ws[f'F{line}'].number_format = '0'

            # Set align - skip column D because it has the title
            for letter in 'ABCEF':
                ws[f'{letter}{line}'].alignment = self.align_center

            # Set border
            for letter in 'ABCDEF':
                ws[f'{letter}{line}'].border = self.border

            # Set fill if line is an even number
            if line % 2 == 0:
                for letter in 'ABCDEF':
                    ws[f'{letter}{line}'].fill = self.fill

            line += 1

        export_filename = f'{subdir}/{product_group.created.day:02} - {product_group.name}.xlsx'

        wb.save(export_filename)
