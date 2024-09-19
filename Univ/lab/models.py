from django.db import models
from django.utils import timezone
# Create your models here.


class MedicineLab(models.Model):
    lab_name=models.CharField(max_length=100,verbose_name='اسم المختبر')
    collage_name=models.CharField(max_length=100,verbose_name='اسم الكلية')
    description=models.TextField(max_length=300,verbose_name='وصف')
    image=models.ImageField(upload_to='medicine/lib/%y/%m/%d',blank=True,verbose_name='صورة')
    
    lab_name_ar=models.CharField(max_length=100,verbose_name='اسم المختبر')
    collage_name_ar=models.CharField(max_length=100,verbose_name='اسم الكلية')
    description_ar=models.TextField(max_length=300,verbose_name='وصف')
    image_ar=models.ImageField(upload_to='medicine/lib/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created_ar=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 


    def __str__(self):
        return self.lab_name
    class Meta:
        verbose_name='مختبر'
        verbose_name_plural='مختبرات كلية الطب'



class EngineerLab(models.Model):
    lab_name=models.CharField(max_length=100,verbose_name='اسم المختبر')
    collage_name=models.CharField(max_length=100,verbose_name='اسم الكلية')
    description=models.TextField(max_length=300,verbose_name='وصف')
    image=models.ImageField(upload_to='medicine/lib/%y/%m/%d',blank=True,verbose_name='صورة')
    
    lab_name_ar=models.CharField(max_length=100,verbose_name='اسم المختبر')
    collage_name_ar=models.CharField(max_length=100,verbose_name='اسم الكلية')
    description_ar=models.TextField(max_length=300,verbose_name='وصف')
    image_ar=models.ImageField(upload_to='medicine/lib/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 


    def __str__(self):
        return self.lab_name

    class Meta:
            verbose_name='مختبر'
            verbose_name_plural='مختبرات كلية الهندسة'


