# Generated by Django 4.1.5 on 2023-04-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentaff', '0008_alter_student_date_created_alter_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('ذكر', 'ذكر'), ('أنثى', 'أنثى')], max_length=50, verbose_name='الجنس'),
        ),
        migrations.AlterField(
            model_name='student',
            name='high_school',
            field=models.CharField(choices=[('علمي', 'علمي'), ('ادبي', 'ادبي')], max_length=50, verbose_name='نوع الثانوية'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id_card_type',
            field=models.CharField(choices=[('بطاقة شخصية', 'بطاقة شخصية'), ('بطاقة عائلية', 'بطاقة عائلية'), (' جواز', 'جواز ')], max_length=50, verbose_name='نوع الهوية'),
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('تقنية معلومات', 'تقنية معلومات'), ('هندسة معمارية', 'هندسة معماري'), ('هندسة مدنية', 'هندسة مدنية'), ('اتصالات', 'اتصالات'), ('هندسة معدات طبية', 'هندسة معدات طبية'), ('هندسة الميكا الكترونكس', 'هندسة الميكاالكترونكس'), ('هندسة النفط والغاز', 'هندسة النفط والغاز'), ('هندسة كيميائية', 'هندسة كيميائية'), ('هندسة مدنية', 'هندسة مدنية'), ('امن معلومات', 'امن معلومات'), ('صيدلة', 'صيدلة'), ('طب بشري', 'طب بشري'), ('مختبرات', 'مختبرات'), ('تمريض', 'تمريض'), ('طب اسنان', 'طب اسنان')], max_length=70, verbose_name='التخصص'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
