'''
This file is used to define the URL patterns for the suppliers app.
'''
from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierUpdateView, \
    SupplierDeleteView, SupplierDetailView

app_name = 'suppliers'
urlpatterns = [
    path('', SupplierListView.as_view(), name='list'),
    path('create/', SupplierCreateView.as_view(), name='create'),
    path('detail/<slug:slug>/', SupplierDetailView.as_view(), name='detail'),
    path('update/<slug:slug>/', SupplierUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>/', SupplierDeleteView.as_view(), name='delete'),
]
