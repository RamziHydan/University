# Generated by Django 4.1.5 on 2023-04-22 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentaff', '0005_alter_student_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='his_phone',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
