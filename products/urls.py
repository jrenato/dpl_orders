'''
This file is used to define the URL patterns for the products app.
'''
from django.urls import path
from .views import ProductFilterView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, ProductReleasesListView, \
    ProductsDebugTemplateView, ProductsWithoutImagesListView, \
    PostponedReleasesListView


app_name = 'products'
urlpatterns = [
    path('debug/', ProductsDebugTemplateView.as_view(), name='debug'),
    path('debug/without-images/', ProductsWithoutImagesListView.as_view(), name='without-images'),

    path('', ProductFilterView.as_view(), name='list'),
    #path('', ProductListView.as_view(), name='list'),
    #path('filter/', ProductFilterView.as_view(), name='filter'),
    path('releases/', ProductReleasesListView.as_view(), name='releases'),
    path('releases/postponed/', PostponedReleasesListView.as_view(), name='releases-postponed'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', ProductUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='delete'),
]
