# Generated by Django 4.1.7 on 2023-02-22 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0017_clickhistrybyuser_remove_clickhistry_userauthdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickhistrybyuser',
            name='userAuthDt',
            field=models.CharField(max_length=254),
        ),
    ]