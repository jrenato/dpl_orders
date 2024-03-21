# Generated by Django 5.0.3 on 2024-03-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_productgroupitem_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='mb_modified',
        ),
        migrations.RemoveField(
            model_name='product',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vl_modified',
        ),
        migrations.AddField(
            model_name='product',
            name='mb_updated',
            field=models.DateField(blank=True, null=True, verbose_name='Metabooks updated at'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='product',
            name='vl_updated',
            field=models.DateField(blank=True, null=True, verbose_name='Vialogos updated at'),
        ),
    ]
