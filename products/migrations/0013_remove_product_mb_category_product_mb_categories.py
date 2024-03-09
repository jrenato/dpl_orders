# Generated by Django 5.0.3 on 2024-03-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_product_internal_id_product_mb_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='mb_category',
        ),
        migrations.AddField(
            model_name='product',
            name='mb_categories',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.productmbcategory', verbose_name='Metabooks Categories'),
        ),
    ]