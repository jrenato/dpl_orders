# Generated by Django 5.0.3 on 2024-03-21 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_product_group'),
        ('products', '0018_rename_is_cover_productimage_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productgroupitem',
            name='group',
        ),
        migrations.RemoveField(
            model_name='productgroupitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductGroup',
        ),
        migrations.DeleteModel(
            name='ProductGroupItem',
        ),
    ]
