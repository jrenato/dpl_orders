from django.urls import path

from orders.views import OrderCreateView, OrderListView, OrderDetailView, \
    OrderDeleteView, OrderUpdateView, OrderItemCreateView, OrderItemUpdateView, \
    OrderItemDeleteView


app_name = 'orders'
urlpatterns = [
    path('', OrderListView.as_view(), name='list'),

    path('<int:pk>/item/create/', OrderItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/update/', OrderItemUpdateView.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='item-delete'),

    path('create/', OrderCreateView.as_view(), name='create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', OrderUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='delete'),
]
