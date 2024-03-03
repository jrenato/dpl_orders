'''
This file is used to define the URL patterns for the products app.
'''
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='delete'),
]
