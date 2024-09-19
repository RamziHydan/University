from django.db import models
from django.utils import timezone
# Create your models here.


#كادر الجامعة
class UnivTeam(models.Model):
    name=models.CharField(max_length=100,verbose_name='الاسم')
    job=models.CharField(max_length=50,verbose_name='الوظيفة')
    vision=models.TextField(default=' ',verbose_name='الرؤية')
    email=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image=models.ImageField(upload_to='Team/%y/%m/%d',blank=True,verbose_name='صورة')
    
    name_ar=models.CharField(max_length=100,verbose_name='الاسم')
    job_ar=models.CharField(max_length=50,verbose_name='الوظيفة')
    vision_ar=models.TextField(default=' ',verbose_name='الرؤية')
    email_ar=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone_ar=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook_ar=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image_ar=models.ImageField(upload_to='Team/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='كادر'
        verbose_name_plural='كادر الجامعة'    






#رؤية الجامعة والرسالة والقيم
class VisionMessage(models.Model):
    #header
    vheader=models.CharField(max_length=100,blank=True,verbose_name='عنوان الرؤية')
    #Description
    vision=models.TextField(max_length=3000,blank=True,verbose_name='الرؤية')
    #header
    mheader=models.CharField(max_length=100,blank=True,verbose_name='عنوان الرسالة')
    #Description
    univmessage=models.TextField(max_length=3000,blank=True,verbose_name='رسالة الجامعة')
    #manner
    image=models.ImageField(upload_to='Vision/%y/%m/%d',blank=True,verbose_name='صورة')
    
    vheader_ar=models.CharField(max_length=100,blank=True,verbose_name='عنوان الرؤية')
    #Description
    vision_ar=models.TextField(max_length=3000,blank=True,verbose_name='الرؤية')
    #header
    mheader_ar=models.CharField(max_length=100,blank=True,verbose_name='عنوان الرسالة')
    #Description
    univmessage_ar=models.TextField(max_length=3000,blank=True,verbose_name='رسالة الجامعة')
    #manner
    image_ar=models.ImageField(upload_to='Vision/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 

    def __str__(self):
        return self.vheader
    class Meta:
        verbose_name='رؤية او رسالة'
        verbose_name_plural='الرؤية والرسالة'


#  اظافة اكثر من عنوان او كلمة او رؤية

class AdditionMessage(models.Model):
    subject=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image=models.ImageField(upload_to='vision/%y/%m/%d',blank=True,verbose_name='صورة')
    
    subject_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image_ar=models.ImageField(upload_to='vision/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 
    
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name='موضع إظافي'
        verbose_name_plural='موضوع إضافي'
#اظافة اكثر من صورة لعرضها عند الحاجة

class AdditonalImage(models.Model):
    photo_name=models.CharField(max_length=30,blank=True,verbose_name='الاسم')
    image=models.ImageField(upload_to='AdditionalImage/%y/%m/%d',blank=True,verbose_name='صورة')
   
    photo_name_ar=models.CharField(max_length=30,blank=True,verbose_name='الاسم')
    image_ar=models.ImageField(upload_to='AdditionalImage/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 

    class Meta:
        verbose_name='صورة'
        verbose_name_plural='صور إظافية'






# السيرة الذاتية لرئيس مجلس الامناء
class BoardPresident(models.Model):
    
    name=models.CharField(max_length=100,blank=True,verbose_name='الاسم')
    Header=models.CharField(max_length=100,blank=True,verbose_name='عنوان')
    #الشهادات 
    studying=models.TextField(max_length=3000,blank=True,verbose_name='السجل الدراسي')
    #مسار وظيفي
    carrier=models.TextField(max_length=3000,blank=True,verbose_name='السجل الوظيفي')

    image=models.ImageField(upload_to='Board/%y/%m/%d',blank=True,verbose_name='صورة')
    
    name_ar=models.CharField(max_length=100,blank=True,verbose_name='الاسم')
    Header_ar=models.CharField(max_length=100,blank=True,verbose_name='عنوان')
    #الشهادات 
    studying_ar=models.TextField(max_length=3000,blank=True,verbose_name='السجل الدراسي')
    #مسار وظيفي
    carrier_ar=models.TextField(max_length=3000,blank=True,verbose_name='السجل الوظيفي')

    image_ar=models.ImageField(upload_to='Board/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='رئيس مجلس امناء'
        verbose_name_plural='رئيس مجلي الامناء'

# كلمة رئيس الجامعة
class UnivPresidentWord(models.Model):
    name=models.CharField(max_length=100,blank=True,verbose_name='الاسم')
    Header=models.CharField(max_length=100,blank=True,verbose_name='العنوان')
    # 
    word=models.TextField(max_length=3000,blank=True,verbose_name='الكلمة')
    image=models.ImageField(upload_to='Univpresident/%y/%m/%d',blank=True,verbose_name='صورة')
    
    name_ar=models.CharField(max_length=100,blank=True,verbose_name='الاسم')
    Header_ar=models.CharField(max_length=100,blank=True,verbose_name='العنوان')
    # 
    word_ar=models.TextField(max_length=3000,blank=True,verbose_name='الكلمة')
    image_ar=models.ImageField(upload_to='Univpresident/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')   
    def __str__(self):
        return self.Header
    class Meta:
        verbose_name='كلمة'
        verbose_name_plural='رئيس الجامعة'
