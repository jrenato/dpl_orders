# Generated by Django 5.0.2 on 2024-02-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0004_remove_supplier_cpf_suppliercnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Company Name'),
        ),
    ]