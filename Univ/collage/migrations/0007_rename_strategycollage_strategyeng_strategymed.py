# Generated by Django 4.2 on 2023-04-21 21:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collage', '0006_alter_strategycollage_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StrategyCollage',
            new_name='StrategyEng',
        ),
        migrations.CreateModel(
            name='StrategyMed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, default='/static/assets/img/hero-bg.jpg', upload_to='medicine/%y/%m/%d')),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('collage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collage.collage')),
            ],
        ),
    ]
