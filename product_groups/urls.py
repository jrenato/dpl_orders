'''
This file is used to define the URL patterns for the products app.
'''
from django.urls import path
from .views import ProductGroupListView, ProductGroupDetailView, ProductGroupCreateView, \
    ProductGroupUpdateView, ProductGroupDeleteView, \
    ProductGroupItemCreateView, ProductGroupItemDeleteView


app_name = 'product_groups'
urlpatterns = [
    path('<slug:slug>/item/create/', ProductGroupItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/delete/', ProductGroupItemDeleteView.as_view(), name='item-delete'),

    path('', ProductGroupListView.as_view(), name='list'),
    path('create/', ProductGroupCreateView.as_view(), name='create'),
    path('<slug:slug>/', ProductGroupDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', ProductGroupUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductGroupDeleteView.as_view(), name='delete'),
]
