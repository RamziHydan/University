# Generated by Django 4.2 on 2023-04-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univinfo', '0007_alter_additonalimage_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additonalimage',
            name='date_created',
            field=models.DateField(blank=True),
        ),
    ]
