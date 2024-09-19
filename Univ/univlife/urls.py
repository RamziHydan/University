from django.urls import path
from .import views

urlpatterns=[
    path('',views.env,name='env'),
    path('perfect',views.perfect,name='perfect'),
    path('service',views.services,name='service'),
    path('guide',views.guide,name='guide'),
    path('env_details/<str:pk>',views.detailsEnv,name='env_details'),
    path('stu_details/<str:pk>',views.detailsStu,name='stu_details'),

    
]