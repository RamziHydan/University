from django.urls import path
from . import views

urlpatterns=[
    # path('',views.DocumentListView.as_view(), name='home'),
    path('', views.DocumentListView.as_view(), name='schedule'),
    path('download/<int:document_id>/',views.download, name='download'),

    path('login',views.studentLogin,name='login'),
]