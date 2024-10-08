# Generated by Django 4.1.5 on 2023-04-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentaff', '0003_remove_student_collage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_place',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='certification_place',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='emission_place',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='governor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='his_phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='reationship',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
