'''
This file is used to define the URL patterns for the customers app.
'''
from django.urls import path

from .views import CustomerListView


app_name = 'customers'
urlpatterns = [
    path('', CustomerListView.as_view(), name='list'),
]
