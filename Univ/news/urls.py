from django.urls import path
from .import views

urlpatterns=[
    path('',views.news,name='news'),
    path('ads',views.ads,name='ads'),
    path('activities',views.activities,name='activities'),
    path('news_details/<str:pk>',views.details,name='news_details'),
    path('ads_details/<str:pk>',views.detailsAds,name='ads_details'),
    path('activities_details/<str:pk>',views.detailsAct,name='activity_details'),
]