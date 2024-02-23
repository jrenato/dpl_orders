'''
Views for the customers app.
'''
from django.views.generic import ListView

from .models import Customer


class CustomerListView(ListView):
    '''
    List view for the customers
    '''
    model = Customer

    context_object_name = 'customers'
    paginate_by = 20
    ordering = ['name']
