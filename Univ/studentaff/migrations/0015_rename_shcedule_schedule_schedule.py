# Generated by Django 4.1.5 on 2023-04-22 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentaff', '0014_rename_name_schedule_collage_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='shcedule',
            new_name='schedule',
        ),
    ]
