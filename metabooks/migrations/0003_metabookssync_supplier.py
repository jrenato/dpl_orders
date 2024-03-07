# Generated by Django 5.0.2 on 2024-03-07 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metabooks', '0002_alter_metabookssync_bearer'),
        ('suppliers', '0010_remove_supplier_internal_id_supplier_mb_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metabookssync',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metabooks_syncs', to='suppliers.supplier'),
        ),
    ]
