from django.shortcuts import render
from lab import models
from news.models import News,Ads
from django.utils.translation import get_language,activate,gettext

# Create your views here.
def index(request):
    trans=translate(language='ar')
    data=models.MedicineLab.objects.all().filter(active=True)
    data1=models.EngineerLab.objects.all().filter(active=True)
    data2=News.objects.all().filter(active=True)
    data3=Ads.objects.all().filter(active=True)
    return render(request,'index.html',{'data':data,'data1':data1,'data2':data2,'data3':data3,'trans':trans})



#تفاصيل الاخبار
def details(request,pk):
    news=News.objects.all().filter(id=pk)
    context={
        'news':news,
        }
    return render(request,'news/news_details.html',context)





def translate(language):
    cur_lang=get_language()
    try:
        activate(language)
    finally:
        activate(cur_lang)
