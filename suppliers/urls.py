'''
This file is used to define the URL patterns for the suppliers app.
'''
from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierUpdateView, \
    SupplierDeleteView, SupplierDetailView

app_name = 'suppliers'
urlpatterns = [
    path('', SupplierListView.as_view(), name='list'),
    path('detail/<int:pk>/', SupplierDetailView.as_view(), name='detail'),
    path('add/', SupplierCreateView.as_view(), name='create'),
    path('update/<int:pk>/', SupplierUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SupplierDeleteView.as_view(), name='delete'),
]
