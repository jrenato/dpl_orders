'''
This is the main URL configuration for the project. It includes the URLs for the
'''
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', login_required(TemplateView.as_view(template_name='home.html'))),

    path('suppliers/', include('suppliers.urls')),
    path('customers/', include('customers.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]
