# Generated by Django 5.0.2 on 2024-03-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetabooksSync',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bearer', models.CharField(max_length=255)),
                ('current_page', models.IntegerField(default=1)),
                ('last_page', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('concluded', models.BooleanField(default=False)),
            ],
        ),
    ]
