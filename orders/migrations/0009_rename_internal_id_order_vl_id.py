# Generated by Django 5.0.3 on 2024-03-07 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_status_alter_orderitem_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='internal_id',
            new_name='vl_id',
        ),
    ]
