# Generated by Django 4.1.5 on 2023-02-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goobusinessesapp', '0008_emailseendb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailseendb',
            name='unicNum',
        ),
        migrations.AddField(
            model_name='emailseendb',
            name='lastseenTime',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='emailseendb',
            name='numberOfSeen',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
