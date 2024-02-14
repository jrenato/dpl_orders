from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView

app_name = 'suppliers'
urlpatterns = [
    path('', SupplierListView.as_view(), name='list'),
    path('add/', SupplierCreateView.as_view(), name='create'),
    path('update/<int:pk>/', SupplierUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', SupplierDeleteView.as_view(), name='delete'),
]
