# Generated by Django 5.0.3 on 2024-04-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customers", "0014_customer_vl_created_customer_vl_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customeraddress",
            name="zip_code",
            field=models.CharField(
                blank=True, max_length=9, null=True, verbose_name="Zip Code"
            ),
        ),
    ]
