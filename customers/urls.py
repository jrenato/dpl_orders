'''
This file is used to define the URL patterns for the customers app.
'''
from django.urls import path

from .views import CustomerListView, CustomerDetailView, CustomerCreateView, \
    CustomerUpdateView, CustomerDeleteView

app_name = 'customers'
urlpatterns = [
    path('', CustomerListView.as_view(), name='list'),
    path('create/', CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete'),
]
