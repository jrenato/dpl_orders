# Generated by Django 5.0.3 on 2024-03-17 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_rename_internal_id_order_vl_id'),
        ('products', '0018_rename_is_cover_productimage_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='products.productgroup', verbose_name='Product Group'),
        ),
    ]
