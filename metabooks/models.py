'''
Models for the MetabooksSync app
'''
from django.db import models


class MetabooksSync(models.Model):
    '''
    Model to store the sync information
    '''
    bearer = models.CharField(max_length=255, blank=True, null=True)
    supplier = models.ForeignKey(
        'suppliers.Supplier', on_delete=models.CASCADE,
        blank=True, null=True, related_name='metabooks_syncs',
    )

    current_page = models.IntegerField(default=1)
    last_page = models.IntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    concluded = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.created} - {self.current_page}/{self.last_page}'
