# Generated by Django 5.0.9 on 2024-10-22 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MetabooksSync",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bearer", models.CharField(blank=True, max_length=255, null=True)),
                ("current_page", models.IntegerField(default=1)),
                ("last_page", models.IntegerField(default=1)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("concluded", models.BooleanField(default=False)),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="metabooks_syncs",
                        to="suppliers.supplier",
                    ),
                ),
            ],
        ),
    ]
