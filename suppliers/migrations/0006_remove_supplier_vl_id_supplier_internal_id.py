# Generated by Django 5.0.2 on 2024-02-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_alter_supplier_options_alter_supplieraddress_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='vl_id',
        ),
        migrations.AddField(
            model_name='supplier',
            name='internal_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Internal id'),
        ),
    ]
