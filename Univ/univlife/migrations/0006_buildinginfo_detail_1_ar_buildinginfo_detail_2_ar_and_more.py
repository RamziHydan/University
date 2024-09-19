# Generated by Django 4.1.5 on 2023-05-06 10:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('univlife', '0005_alter_buildinginfo_options_alter_perfectstu_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinginfo',
            name='detail_1_ar',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل 1'),
        ),
        migrations.AddField(
            model_name='buildinginfo',
            name='detail_2_ar',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل 2'),
        ),
        migrations.AddField(
            model_name='buildinginfo',
            name='detail_3_ar',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل 3'),
        ),
        migrations.AddField(
            model_name='buildinginfo',
            name='image_ar',
            field=models.ImageField(blank=True, upload_to='buildingImage/%y/%m/%d', verbose_name='صورة'),
        ),
        migrations.AddField(
            model_name='buildinginfo',
            name='name_ar',
            field=models.CharField(blank=True, max_length=40, verbose_name='الاسم'),
        ),
        migrations.AddField(
            model_name='buildinginfo',
            name='title_ar',
            field=models.CharField(blank=True, max_length=40, verbose_name='عنوان'),
        ),
        migrations.AddField(
            model_name='perfectstu',
            name='detail_ar',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل'),
        ),
        migrations.AddField(
            model_name='perfectstu',
            name='header_ar',
            field=models.CharField(default=1, max_length=40, verbose_name='موضوع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfectstu',
            name='image_ar',
            field=models.ImageField(blank=True, upload_to='perfectStudent/%y/%m/%d', verbose_name='صورة'),
        ),
        migrations.AddField(
            model_name='perfectstu',
            name='title_ar',
            field=models.CharField(blank=True, max_length=40, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='active',
            field=models.BooleanField(default=True, verbose_name='متوفر'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الانشاء'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='detail_1',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل 1'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='detail_2',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل 2'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='detail_3',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل 3'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='buildingImage/%y/%m/%d', verbose_name='صورة'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='name',
            field=models.CharField(blank=True, max_length=40, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='buildinginfo',
            name='title',
            field=models.CharField(blank=True, max_length=40, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='perfectstu',
            name='active',
            field=models.BooleanField(default=True, verbose_name='متوفر'),
        ),
        migrations.AlterField(
            model_name='perfectstu',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الانشاء'),
        ),
        migrations.AlterField(
            model_name='perfectstu',
            name='detail',
            field=models.TextField(blank=True, max_length=400, verbose_name='تفاصيل'),
        ),
        migrations.AlterField(
            model_name='perfectstu',
            name='header',
            field=models.CharField(max_length=40, verbose_name='موضوع'),
        ),
        migrations.AlterField(
            model_name='perfectstu',
            name='image',
            field=models.ImageField(blank=True, upload_to='perfectStudent/%y/%m/%d', verbose_name='صورة'),
        ),
        migrations.AlterField(
            model_name='perfectstu',
            name='title',
            field=models.CharField(blank=True, max_length=40, verbose_name='عنوان'),
        ),
    ]
