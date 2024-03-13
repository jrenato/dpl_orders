'''
This file is used to define the URL patterns for the products app.
'''
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, \
    ProductGroupListView, ProductGroupDetailView, ProductGroupCreateView, \
    ProductGroupUpdateView, ProductGroupDeleteView, \
    ProductsDebugTemplateView, ProductsWithoutImagesListView


app_name = 'products'
urlpatterns = [
    path('debug/', ProductsDebugTemplateView.as_view(), name='debug'),
    path('debug/without-images/', ProductsWithoutImagesListView.as_view(), name='without-images'),

    path('group/', ProductGroupListView.as_view(), name='group-list'),
    path('group/create/', ProductGroupCreateView.as_view(), name='group-create'),
    path('group/<int:pk>/', ProductGroupDetailView.as_view(), name='group-detail'),
    path('group/<int:pk>/update/', ProductGroupUpdateView.as_view(), name='group-update'),
    path('group/<int:pk>/delete/', ProductGroupDeleteView.as_view(), name='group-delete'),

    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='delete'),
]
