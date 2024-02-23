'''
This is the main URL configuration for the project. It includes the URLs for the
'''
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('suppliers/', include('suppliers.urls')),
    path('customers/', include('customers.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]
