# Generated by Django 5.0.3 on 2024-03-04 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_productgroupitem_group_and_more'),
        ('suppliers', '0009_alter_supplier_person_or_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='suppliers.supplier', verbose_name='Supplier'),
        ),
    ]