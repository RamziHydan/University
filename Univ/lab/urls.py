from django.urls import path
from .import views

urlpatterns=[
    path('',views.medLab,name='medlab'),
    path('englab',views.engLab,name='englab'),
]