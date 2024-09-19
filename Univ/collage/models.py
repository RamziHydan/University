from django.db import models
from django.utils import timezone


class Collage(models.Model):
    name=models.CharField(max_length=40,null=True,verbose_name='الاسم')
    vision=models.TextField(max_length=3000,blank=True,verbose_name='الرؤية')
    message=models.TextField(max_length=3000,blank=True,verbose_name='الرسالة')
    strategy=models.TextField(max_length=1000,blank=True,verbose_name='الاستراتيجية')
    description=models.TextField(max_length=400,blank=True,verbose_name='وصف')
    image=models.ImageField(upload_to='collage/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')

    name_ar=models.CharField(max_length=40,null=True,verbose_name='الاسم')
    vision_ar=models.TextField(max_length=3000,blank=True,verbose_name='الرؤية')
    message_ar=models.TextField(max_length=3000,blank=True,verbose_name='الرسالة')
    strategy_ar=models.TextField(max_length=1000,blank=True,verbose_name='الاستراتيجية')
    description_ar=models.TextField(max_length=400,blank=True,verbose_name='وصف')
    image_ar=models.ImageField(upload_to='collage/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    active=models.BooleanField(default=True,verbose_name='متوفر') 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='كلية'
        verbose_name_plural='الكليات'




class MedicineMajor(models.Model):
    MAJOR=(
        ('صيدلة','صيدلة'),
        ('طب بشري','طب بشري'),
        ('مختبرات','مختبرات'),
        ('تمريض','تمريض'),
        ('طب اسنان','طب اسنان'),
    )
    collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True,verbose_name='الكلية')
    category=models.CharField(max_length=50,choices=MAJOR,verbose_name='التخصص')
    majorinfo=models.TextField(max_length=3000,blank=True,verbose_name='معلومات التخصص')
    goals=models.TextField(max_length=300,blank=True,verbose_name='الاهداف')
    sectionunivinfo=models.TextField(max_length=3000,blank=True,verbose_name='معلومات عن القسم الجامعي')
    image=models.ImageField(upload_to='medicine/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    
    category_ar=models.CharField(max_length=50,choices=MAJOR,verbose_name='التخصص')
    majorinfo_ar=models.TextField(max_length=3000,blank=True,verbose_name='معلومات التخصص')
    goals_ar=models.TextField(max_length=300,blank=True,verbose_name='الاهداف')
    sectionunivinfo_ar=models.TextField(max_length=3000,blank=True,verbose_name='معلومات عن القسم الجامعي')
    image_ar=models.ImageField(upload_to='medicine/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created_ar=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')

    def __str__(self):
        return self.category
    class Meta:
        verbose_name='تخصص'
        verbose_name_plural='كلية الطب'


class EngineerMajor(models.Model):
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
    )
    collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True,verbose_name='الكلية')
    category=models.CharField(max_length=70,choices=MAJOR,verbose_name='التخصص')
    image=models.ImageField(upload_to='ُEngineer/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    majorinfo=models.TextField(max_length=3000,blank=True,verbose_name='معلومات التخصص')
    goals=models.TextField(max_length=300,blank=True,verbose_name='الاهداف')
    sectionunivinfo=models.TextField(max_length=3000,blank=True,verbose_name='معلومات القسم الجامعي')
    
    
    category_ar=models.CharField(max_length=70,choices=MAJOR,verbose_name='التخصص')

    image_ar=models.ImageField(upload_to='ُEngineer/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    majorinfo_ar=models.TextField(max_length=3000,blank=True,verbose_name='معلومات التخصص')
    goals_ar=models.TextField(max_length=300,blank=True,verbose_name='الاهداف')
    sectionunivinfo_ar=models.TextField(max_length=3000,blank=True,verbose_name='معلومات القسم الجامعي')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name='كلية'
        verbose_name_plural='كلية الهندسة'



class HumanityMajor(models.Model):
    MAJOR=(
        ('اللغات','اللغات'),
        ('علم النفس','علم النفس'),
        ('علم الاجتماع','علم الاجتماع'),
        ('الشريعة والدراسات الاسلامية','الشريعة والدراسات الاسلامية'),
        ('اللغة العربية','اللغة العربية'),
        ('قسم علم الاجتماع والخدمة الاجتماعية','قسم علم الاجتماع والخدمة الاجتماعية'),
        ('قسم الجغرافيا ونظم المعلومات الجغرافية','قسم الجغرافيا ونظم المعلومات الجغرافية'),
        ('قسم التاريــخ','قسم التاريــخ'),
        ('قسم علم الاجتماع والخدمة الاجتماعية','قسم علم الاجتماع والخدمة الاجتماعية'),
        
    )
    collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True,verbose_name='الكلية')
    category=models.CharField(max_length=70,choices=MAJOR,verbose_name='التخصص')
    image=models.ImageField(upload_to='Humanities/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    majorinfo=models.TextField(max_length=3000,blank=True,verbose_name='معلومات التخصص')
    goals=models.TextField(max_length=300,blank=True,verbose_name='الاهداف')
    sectionunivinfo=models.TextField(max_length=3000,blank=True,verbose_name='معلومات القسم الجامعي')
    
    category_ar=models.CharField(max_length=70,choices=MAJOR,verbose_name='التخصص')
    image_ar=models.ImageField(upload_to='Humanities/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    majorinfo_ar=models.TextField(max_length=3000,blank=True,verbose_name='معلومات التخصص')
    goals_ar=models.TextField(max_length=300,blank=True,verbose_name='الاهداف')
    sectionunivinfo_ar=models.TextField(max_length=3000,blank=True,verbose_name='معلومات القسم الجامعي')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name='كلية'
        verbose_name_plural='كلية العلوم الانسانية'


class CollageHumTeam(models.Model):
    name=models.CharField(max_length=100,verbose_name='الاسم')
    job=models.CharField(max_length=50,verbose_name='الوظيفة')
    email=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image=models.ImageField(upload_to='humTeam/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    
    name_ar=models.CharField(max_length=100,verbose_name='الاسم')
    job_ar=models.CharField(max_length=50,verbose_name='الوظيفة')
    email_ar=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook_ar=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image_ar=models.ImageField(upload_to='humTeam/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='كادر'
        verbose_name_plural='كادر كلية العلوم الانسانية'



#  اظافة اكثر من عنوان او كلمة او رؤية

class AdditionMessage(models.Model):
    subject=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    subject_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image=models.ImageField(upload_to='vision/%y/%m/%d',blank=True,verbose_name='صورة')
    image_ar=models.ImageField(upload_to='vision/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 
    def __str__(self):
        return self.subject

    class Meta:
        verbose_name='رسالة إضافية'
        verbose_name_plural='رسائل إضافية'

class StrategyMed(models.Model):
    collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True,verbose_name='الكلية')
    subject=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image=models.ImageField(upload_to='medicine/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    
    subject_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image_ar=models.ImageField(upload_to='medicine/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name='إستراتيجية'
        verbose_name_plural='إستراتيجية كلية الطب'

class StrategyHum(models.Model):
    collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True,verbose_name='الكلية ')
    subject=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image=models.ImageField(upload_to='Humanty/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    
    subject_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image_ar=models.ImageField(upload_to='Humanty/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name='إستراتيجية'
        verbose_name_plural='إستراتيجية كليةالعلوم'

class StrategyEng(models.Model):
    collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True,verbose_name='الكلية')
    subject=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image=models.ImageField(upload_to='medicine/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    
    subject_ar=models.TextField(max_length=500,blank=True,verbose_name='موضوع')
    image_ar=models.ImageField(upload_to='medicine/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')
    def __str__(self):
        return self.subject
    class Meta:
        verbose_name='إستراتيجية'
        verbose_name_plural='إستراتيجيةكلية الهندسة'
#اظافة اكثر من صورة لعرضها عند الحاجة

class AdditonalImage(models.Model):
    photo_name=models.CharField(max_length=30,blank=True,verbose_name='اسم الصورة')
    image=models.ImageField(upload_to='AdditionalImage/%y/%m/%d',blank=True,verbose_name='صورة')
    
    photo_name_ar=models.CharField(max_length=30,blank=True,verbose_name='اسم الصورة')
    image_ar=models.ImageField(upload_to='AdditionalImage/%y/%m/%d',blank=True,verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر') 
    
    class Meta:
        verbose_name='صورة إظافية'
        verbose_name_plural='صور إظافية'    





class CollageMedTeam(models.Model):
    name=models.CharField(max_length=100,verbose_name='الاسم')
    job=models.CharField(max_length=50,verbose_name='الوظيفة')
    email=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image=models.ImageField(upload_to='medTeam/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    
    name_ar=models.CharField(max_length=100,verbose_name='الاسم')
    job_ar=models.CharField(max_length=50,verbose_name='الوظيفة')
    email_ar=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone_ar=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook_ar=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image_ar=models.ImageField(upload_to='medTeam/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='كادر'
        verbose_name_plural='كادر كلية الطب'
    




class CollageEngTeam(models.Model):
    name=models.CharField(max_length=100,verbose_name='الاسم')
    job=models.CharField(max_length=50,verbose_name='الوظيفة')
    email=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image=models.ImageField(upload_to='engTeam/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    
    name_ar=models.CharField(max_length=100,verbose_name='الاسم')
    job_ar=models.CharField(max_length=50,verbose_name='الوظيفة')
    email_ar=models.EmailField(max_length=150,blank=True,verbose_name='البريد')
    phone_ar=models.IntegerField(null=True,verbose_name='الهاتف')
    facebook_ar=models.CharField(max_length=150,blank=True,verbose_name='الفيسبوك')
    image_ar=models.ImageField(upload_to='engTeam/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg",verbose_name='صورة')
    date_created=models.DateField(default=timezone.now,verbose_name='تاريخ الانشاء')
    active=models.BooleanField(default=True,verbose_name='متوفر')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name='كادر'
        verbose_name_plural='كادر كلية الهندسة'
    
    


# class Major(models.Model):
#     name=models.CharField(max_length=40,blank=True)
#     collage=models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True)
#     image=models.ImageField(upload_to='collage/%y/%m/%d',blank=True,default="/static/assets/img/hero-bg.jpg")
#     majorinfo=models.TextField(max_length=3000,blank=True)
#     goals=models.TextField(max_length=300,blank=True)
#     sectionunivinfo=models.TextField(max_length=3000,blank=True)
#     date_created=models.DateField(default=timezone.now)
#     active=models.BooleanField(default=True)

#     def __str__(self):
#         return self.name