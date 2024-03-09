# Generated by Django 5.0.3 on 2024-03-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_mb_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='internal_id',
        ),
        migrations.AddField(
            model_name='product',
            name='mb_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Metabooks id'),
        ),
        migrations.AddField(
            model_name='product',
            name='vl_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Vialogos id'),
        ),
    ]
