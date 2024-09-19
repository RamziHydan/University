from django.db import models
from django.utils import timezone
# Create your models here.


# البيئة الجامعية
class BuildingInfo(models.Model):
    name=models.CharField(max_length=40,blank=True,verbose_name='الاسم')
    title=models.CharField(max_length=40,blank=True,verbose_name='عنوان')
    detail_1=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل 1')
    detail_2=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل 2')
    detail_3=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل 3')
    image=models.ImageField(upload_to='buildingImage/%y/%m/%d',blank=True,verbose_name='صورة')
    
    name_ar=models.CharField(max_length=40,blank=True,verbose_name='الاسم')
    title_ar=models.CharField(max_length=40,blank=True,verbose_name='عنوان')
    detail_1_ar=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل 1')
    detail_2_ar=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل 2')
    detail_3_ar=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل 3')
    image_ar=models.ImageField(upload_to='buildingImage/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='مبنى او منشاءة جامعية'
        verbose_name_plural='البيئة الجامعية'


class PerfectStu(models.Model):
    header=models.CharField(max_length=40,verbose_name='موضوع')
    title=models.CharField(max_length=40,blank=True,verbose_name='عنوان')
    detail=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل')
    image=models.ImageField(upload_to='perfectStudent/%y/%m/%d',blank=True,verbose_name='صورة')
    
    header_ar=models.CharField(max_length=40,verbose_name='موضوع')
    title_ar=models.CharField(max_length=40,blank=True,verbose_name='عنوان')
    detail_ar=models.TextField(max_length=400,blank=True,verbose_name='تفاصيل')
    image_ar=models.ImageField(upload_to='perfectStudent/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 
    def __str__(self):
        return self.header
    

    class Meta:
        verbose_name='طلاب اوائل'
        verbose_name_plural='الطلاب الاوائل'