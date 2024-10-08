# Generated by Django 4.2 on 2023-04-23 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='activities/%y/%m/%d')),
                ('subject', models.TextField(blank=True, max_length=500)),
                ('subject_1', models.TextField(blank=True, max_length=500)),
                ('subject_2', models.TextField(blank=True, max_length=500)),
                ('subject_3', models.TextField(blank=True, max_length=500)),
                ('subject_4', models.TextField(blank=True, max_length=500)),
                ('subject_5', models.TextField(blank=True, max_length=500)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='ads/%y/%m/%d')),
                ('subject', models.TextField(blank=True, max_length=500)),
                ('subject_1', models.TextField(blank=True, max_length=500)),
                ('subject_2', models.TextField(blank=True, max_length=500)),
                ('subject_3', models.TextField(blank=True, max_length=500)),
                ('subject_4', models.TextField(blank=True, max_length=500)),
                ('subject_5', models.TextField(blank=True, max_length=500)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='news/%y/%m/%d')),
                ('subject', models.TextField(blank=True, max_length=500)),
                ('subject_1', models.TextField(blank=True, max_length=500)),
                ('subject_2', models.TextField(blank=True, max_length=500)),
                ('subject_3', models.TextField(blank=True, max_length=500)),
                ('subject_4', models.TextField(blank=True, max_length=500)),
                ('subject_5', models.TextField(blank=True, max_length=500)),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
