'''
This is the main URL configuration for the project. It includes the URLs for the
'''
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('suppliers/', include('suppliers.urls')),
    path('customers/', include('customers.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]
