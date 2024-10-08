# Generated by Django 4.1.5 on 2023-05-05 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentaff', '0017_document_delete_schedule'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'جدول', 'verbose_name_plural': 'الجداول'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'طالب', 'verbose_name_plural': 'الطلاب المسجلين في الجامعة'},
        ),
        migrations.AlterField(
            model_name='document',
            name='active',
            field=models.BooleanField(default=True, verbose_name='متوفر'),
        ),
        migrations.AlterField(
            model_name='document',
            name='collage_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='الكلية'),
        ),
        migrations.AlterField(
            model_name='document',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الانشاء'),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', verbose_name='الجدول'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, max_length=100, verbose_name='العنوان'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الميلاد'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birth_place',
            field=models.CharField(blank=True, max_length=50, verbose_name='مكان الميلاد'),
        ),
        migrations.AlterField(
            model_name='student',
            name='card_number',
            field=models.CharField(max_length=50, verbose_name='رقم الهوية'),
        ),
        migrations.AlterField(
            model_name='student',
            name='certification_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الحصول على الشهادة'),
        ),
        migrations.AlterField(
            model_name='student',
            name='certification_place',
            field=models.CharField(blank=True, max_length=100, verbose_name='مكان الحصول على الشهادة'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=100, verbose_name='البريد'),
        ),
        migrations.AlterField(
            model_name='student',
            name='emission_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاريخ الاصدار'),
        ),
        migrations.AlterField(
            model_name='student',
            name='emission_place',
            field=models.CharField(blank=True, max_length=50, verbose_name='مكان الاصدار'),
        ),
        migrations.AlterField(
            model_name='student',
            name='governor',
            field=models.CharField(blank=True, max_length=50, verbose_name='المحافظة'),
        ),
        migrations.AlterField(
            model_name='student',
            name='his_phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='هاتف ولي الامر'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=150, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=150, verbose_name='الجنسية'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='الهاتف'),
        ),
        migrations.AlterField(
            model_name='student',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='المعدل'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reationship',
            field=models.CharField(blank=True, max_length=100, verbose_name='ولي الامر'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.CharField(blank=True, max_length=50, verbose_name='المدرسة'),
        ),
    ]
