from django.db import models
from django.utils import timezone
# Create your models here.

#الاخبار
class News(models.Model):
    title=models.CharField(max_length=40,verbose_name='عنوان')
    image=models.ImageField(upload_to='news/%y/%m/%d',blank=True,verbose_name='صورة')
    subject=models.CharField(max_length=30,blank=True,verbose_name='موضوع')
    subject_1=models.TextField(max_length=500,blank=True,verbose_name='موضوع 1')
    subject_2=models.TextField(max_length=500,blank=True,verbose_name='موضوع 2')
    subject_3=models.TextField(max_length=500,blank=True,verbose_name='موضوع 3')
    subject_4=models.TextField(max_length=500,blank=True,verbose_name='موضوع 4')
    subject_5=models.TextField(max_length=500,blank=True,verbose_name='موضوع 5')
    
    title_ar=models.CharField(max_length=40,verbose_name='عنوان')
    image_ar=models.ImageField(upload_to='news/%y/%m/%d',blank=True,verbose_name='صورة')
    subject_ar=models.CharField(max_length=30,blank=True,verbose_name='موضوع')
    subject_1_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 1')
    subject_2_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 2')
    subject_3_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 3')
    subject_4_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 4')
    subject_5_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 5')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='خبر'
        verbose_name_plural='الاخبار'


#الاعلانات
class Ads(models.Model):
    title=models.CharField(max_length=40,verbose_name='عنوان')
    image=models.ImageField(upload_to='ads/%y/%m/%d',blank=True,verbose_name='صورة')
    subject=models.CharField(max_length=500,blank=True,verbose_name='موضوع')
    subject_1=models.TextField(max_length=500,blank=True,verbose_name='موضوع 1')
    subject_2=models.TextField(max_length=500,blank=True,verbose_name='موضوع 2')
    subject_3=models.TextField(max_length=500,blank=True,verbose_name='موضوع 3')
    subject_4=models.TextField(max_length=500,blank=True,verbose_name='موضوع 4')
    subject_5=models.TextField(max_length=500,blank=True,verbose_name='موضوع 5')
    
    title_ar=models.CharField(max_length=40,verbose_name='عنوان')
    image_ar=models.ImageField(upload_to='ads/%y/%m/%d',blank=True,verbose_name='صورة')
    subject_ar=models.CharField(max_length=500,blank=True,verbose_name='موضوع')
    subject_1_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 1')
    subject_2_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 2')
    subject_3_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 3')
    subject_4_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 4')
    subject_5_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 5')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='إعلان'
        verbose_name_plural='الإعلانات'


#انشطة وفعاليات
class Activities(models.Model):
    title=models.CharField(max_length=40,verbose_name='عنوان')
    image=models.ImageField(upload_to='activities/%y/%m/%d',blank=True,verbose_name='صورة')
    subject=models.CharField(max_length=500,blank=True,verbose_name='موضوع')
    subject_1=models.TextField(max_length=500,blank=True,verbose_name='موضوع 1')
    subject_2=models.TextField(max_length=500,blank=True,verbose_name='موضوع 2')
    subject_3=models.TextField(max_length=500,blank=True,verbose_name='موضوع 3')
    subject_4=models.TextField(max_length=500,blank=True,verbose_name='موضوع 4')
    subject_5=models.TextField(max_length=500,blank=True,verbose_name='موضوع 5')
    
    title_ar=models.CharField(max_length=40,verbose_name='عنوان')
    image_ar=models.ImageField(upload_to='activities/%y/%m/%d',blank=True,verbose_name='صورة')
    subject_ar=models.CharField(max_length=500,blank=True,verbose_name='موضوع')
    subject_1_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 1')
    subject_2_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 2')
    subject_3_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 3')
    subject_4_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 4')
    subject_5_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع 5')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 


    def __str__(self):
        return self.title
    class Meta:
        verbose_name='نشاط او فعالية'
        verbose_name_plural='الانشطة والفعاليات'