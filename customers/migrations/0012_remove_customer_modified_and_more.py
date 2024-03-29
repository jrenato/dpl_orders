# Generated by Django 5.0.3 on 2024-03-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_rename_internal_id_customer_vl_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='customerphone',
            name='modified',
        ),
        migrations.AddField(
            model_name='customer',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='customeraddress',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='customerphone',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
