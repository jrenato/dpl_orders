# Generated by Django 5.0.3 on 2024-03-07 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_alter_customer_person_or_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='internal_id',
            new_name='vl_id',
        ),
    ]
