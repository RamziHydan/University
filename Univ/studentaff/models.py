from django.db import models
from collage.models import *
from django.utils import timezone
# Create your models here.
from django.utils.translation import gettext_lazy as _
class Student(models.Model):
    MAJOR=(
        ('تقنية معلومات','تقنية معلومات'),
        ('هندسة معمارية','هندسة معماري'),
        ('هندسة مدنية','هندسة مدنية'),
        ('اتصالات','اتصالات'),
        ('هندسة معدات طبية','هندسة معدات طبية'),
        ('هندسة الميكا الكترونكس','هندسة الميكاالكترونكس'),
        ('هندسة النفط والغاز','هندسة النفط والغاز'),
        ('هندسة كيميائية','هندسة كيميائية'),
        ('هندسة مدنية','هندسة مدنية'),
        ('امن معلومات','امن معلومات'),
        ('صيدلة','صيدلة'),
        ('طب بشري','طب بشري'),
        ('مختبرات','مختبرات'),
        ('تمريض','تمريض'),
        ('طب اسنان','طب اسنان'),
    )
    GENDER=(
        ('ذكر','ذكر'),
        ('أنثى','أنثى'),        
    )
    CATEGORY=(
        ('علمي','علمي'),
        ('ادبي','ادبي'),        
    )
    IDENTIFICATIONS=(
        ('بطاقة شخصية','بطاقة شخصية'),
        ('بطاقة عائلية','بطاقة عائلية'),        
        (' جواز','جواز '),        
    )
    name=models.CharField(max_length=150,verbose_name=_('Name'))
    gender=models.CharField(max_length=50,choices=GENDER,verbose_name=_('Gender'))
    nationality=models.CharField(max_length=150,blank=True,verbose_name=_('Nationality'))
    birth_place=models.CharField(max_length=50,blank=True,verbose_name=_('Birth place'))
    birth_date=models.DateField(default=timezone.now,verbose_name=_('Birth date'))
    high_school=models.CharField(max_length=50,choices=CATEGORY,verbose_name=_('High school ype'))
    rate=models.DecimalField(max_digits=4,decimal_places=2,verbose_name=_('rate'))
    certification_date=models.DateField(default=timezone.now,verbose_name=_('Certification date'))
    certification_place=models.CharField(max_length=100,blank=True,verbose_name=_('Certification place'))
    governor=models.CharField(max_length=50,blank=True,verbose_name=_('governer'))
    school=models.CharField(max_length=50,blank=True,verbose_name=_('School'))
    emission_place=models.CharField(max_length=50,blank=True,verbose_name=_('Emission date'))
    emission_date=models.DateField(default=timezone.now,verbose_name=_('Emission place'))
    #contact us
    phone=models.CharField(max_length=30, blank=True,verbose_name=_('Phone'))
    address=models.TextField(max_length=100,blank=True,verbose_name=_('Address'))
    email=models.EmailField(max_length=100,blank=True,verbose_name=_('Email'))
    reationship=models.CharField(max_length=100,blank=True,verbose_name=_('Relationship'))
    his_phone=models.CharField(max_length=30, blank=True,verbose_name=_('Relationship Phone'))
    #major
    # collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True)
    major=models.CharField(max_length=70,choices=MAJOR,verbose_name=_('Major'))
    # identification card
    id_card_type=models.CharField(max_length=50,choices=IDENTIFICATIONS,verbose_name=_('ID type'))
    card_number=models.CharField(max_length=50,verbose_name=_('ID number'))
    # date_created=models.DateField(auto_now_add=True,editable=False)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name='طالب'
        verbose_name_plural='الطلاب المسجلين في الجامعة'





class Document(models.Model):
    collage_name=models.CharField(max_length=40,blank=True,verbose_name='الكلية')
    document = models.FileField(upload_to='documents/',verbose_name='الجدول')
    collage_name_ar=models.CharField(max_length=40,blank=True,verbose_name='الكلية')
    document_ar= models.FileField(upload_to='documents/',verbose_name='الجدول')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')

    def __str__(self) :
        return self.collage_name
    class Meta:
        verbose_name='جدول'
        verbose_name_plural='الجداول'