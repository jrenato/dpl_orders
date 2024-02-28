# Generated by Django 5.0.2 on 2024-02-28 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_supplier_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='emailnfe',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email NFe'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='municipal_registration',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Municipal Registration'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='person_or_company',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Person or Company'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='state_registration',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='State Registration'),
        ),
        migrations.AddField(
            model_name='supplieraddress',
            name='district',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='District'),
        ),
        migrations.CreateModel(
            name='SupplierPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier')),
            ],
            options={
                'verbose_name': 'Supplier Phone',
                'verbose_name_plural': 'Supplier Phones',
                'ordering': ['supplier', 'phone_number'],
            },
        ),
    ]
