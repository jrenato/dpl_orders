# Generated by Django 5.0.2 on 2024-02-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
