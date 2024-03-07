from django.contrib import admin

from .models import MetabooksSync


@admin.register(MetabooksSync)
class MetabooksSyncAdmin(admin.ModelAdmin):
    '''
    Admin class for MetabooksSync
    '''
    list_display = (
        'id', 'supplier', 'current_page', 'last_page',
        'concluded', 'created', 'updated'
    )
