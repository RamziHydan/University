from django.urls import path
# from django.conf.urls import url 
from . import views
urlpatterns=[
    #رابط صفحة الكليات
    path('',views.collage,name='collage'),




    ####      روابط صفحات الهندسة     ####
    
    # رابط الصفحة العامة للهندسة
    path('engineering',views.engineering,name='engineering'),
    #رابط صفحات تخصصات الهندسة
    path('major',views.major,name='major'),
    #رابط صفحة مكتبة كلية الهندسة
    path('collagelib',views.collagelib,name='collagelib'),
    #رابط صفحة استراتيجية الكلية
    path('strategy',views.strategy,name='strategy'),
    # رابط صفحة كادر الكلية
    path('team',views.team,name='team'),


    ####      روابط صفحات العلوم الانسانية     ####
    
    #رابط الصفحة العامة العلوم
    path('hum',views.humanities,name='hum'),
    #رابط صفحات تخصصات العلوم
    path('hmajor',views.hmajor,name='hmajor'),
    #رابط صفحة مكتبة كلية  العلوم
    path('hcollagelib',views.collhumlib,name='hcollagelib'),
    #رابط صفحة استراتيجية الكلية
    path('hstrategy',views.hstrategy,name='hstrategy'),
    # رابط صفحة كادر الكلية
    path('hteam',views.hteam,name='hteam'),





    ####      روابط صفحات الطب     ####

    # رابط الصفحة العامة للطب
    path('medicine',views.medicine,name='medicine'),
    #رابط صفحات تخصصات الطب
    path('majorm',views.majorm,name='majorm'),
    # path('majorm/<str:pk>',views.majorm,name='majorm'),

    #رابط صفحة مكتبة كلية الطب
    path('collagelibm',views.collagelibm,name='collagelibm'),
    #رابط صفحة استراتيجية الكلية
    path('strategym',views.strategym,name='strategym'),
    # رابط صفحة كادر الكلية
    path('teamm',views.teamm,name='teamm'),

    
]