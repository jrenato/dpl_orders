# Generated by Django 5.0.2 on 2024-02-23 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='slug',
            field=models.SlugField(max_length=140, unique=True, verbose_name='Slug'),
        ),
    ]