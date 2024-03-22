# Generated by Django 5.0.3 on 2024-03-21 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_order_product_group'),
        ('product_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='product_groups.productgroup', verbose_name='Product Group'),
        ),
    ]