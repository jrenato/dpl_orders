'''
This file is used to define the URL patterns for the customers app.
'''
from django.urls import path

from .views import CustomerListView, CustomerDetailView, CustomerCreateView, \
    CustomerUpdateView, CustomerDeleteView, CustomerPhoneCreateView, CustomerPhoneUpdateView, \
    CustomerPhoneDeleteView

app_name = 'customers'
urlpatterns = [
    path('', CustomerListView.as_view(), name='list'),
    path('create/', CustomerCreateView.as_view(), name='create'),
    path('<slug:slug>/', CustomerDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', CustomerUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', CustomerDeleteView.as_view(), name='delete'),
    path('<slug:slug>/add_phone/', CustomerPhoneCreateView.as_view(), name='add_phone'),
    path('update_phone/<int:pk>/', CustomerPhoneUpdateView.as_view(), name='update_phone'),
    path('delete_phone/<int:pk>/', CustomerPhoneDeleteView.as_view(), name='delete_phone'),
]
