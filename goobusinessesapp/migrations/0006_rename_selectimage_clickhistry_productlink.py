# Generated by Django 4.1.5 on 2023-01-31 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0005_aboutdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clickhistry',
            old_name='selectImage',
            new_name='productLink',
        ),
    ]
