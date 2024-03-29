# Generated by Django 5.0.2 on 2024-03-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_orderitem_delivered_quantity_orderitem_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('IS', 'In Separation'), ('WC', 'Waiting for Confirmation'), ('IN', 'Invoiced'), ('WT', 'Waiting Transport'), ('FI', 'Finished'), ('CA', 'Canceled')], default='PE', max_length=2),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('FI', 'Finished'), ('CA', 'Canceled')], default='PE', max_length=2),
        ),
        migrations.AlterField(
            model_name='orderstatushistory',
            name='status',
            field=models.CharField(choices=[('PE', 'Pending'), ('IS', 'In Separation'), ('WC', 'Waiting for Confirmation'), ('IN', 'Invoiced'), ('WT', 'Waiting Transport'), ('FI', 'Finished'), ('CA', 'Canceled')], default='PE', max_length=2),
        ),
    ]
