from django.urls import path
from . import views
urlpatterns=[
    #الرؤية والرسالة
    path('',views.vision,name='vision'),
    #سيرة رئيس مجلس الامناء
    path('board',views.boardpre,name='board'),
    #كلمة رئيس الجامع
    path('univpre',views.univpre,name='univpre'),
    #كادر الجامعة
    path('Univteam',views.univteam,name='Univteam'),
    # تفاصيل كادر الجامعة
    path('tem_details/<str:pk>',views.detailsTem,name='tem_details'),

]