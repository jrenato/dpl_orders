'''
This file is used to define the URL patterns for the customers app.
'''
from django.urls import path

from .views import CustomerListView, CustomerDetailView, CustomerCreateView, \
    CustomerUpdateView, CustomerDeleteView, update_customer

app_name = 'customers'
urlpatterns = [
    path('', CustomerListView.as_view(), name='list'),
    path('create/', CustomerCreateView.as_view(), name='create'),
    path('<slug:slug>/', CustomerDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', CustomerUpdateView.as_view(), name='update'),
    path('<slug:slug>/update_customer/', update_customer, name='update_customer'),
    path('<slug:slug>/delete/', CustomerDeleteView.as_view(), name='delete'),
]
