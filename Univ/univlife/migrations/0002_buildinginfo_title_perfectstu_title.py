# Generated by Django 4.2 on 2023-04-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univlife', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinginfo',
            name='title',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='perfectstu',
            name='title',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
