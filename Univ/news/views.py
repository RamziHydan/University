from django.shortcuts import render
from .models import News,Ads,Activities
# Create your views here.

# الاخبار
def news(request):
    data=News.objects.all().filter(active=True)
    context={'data':data}
    return render(request,'news/news.html',context)


#الاعلانات
def ads(request):
    data=Ads.objects.all().filter(active=True)
    context={'data':data}
    return render(request,'news/ads.html',context)

# انشطة وفعاليات
def activities(request):
    data=Activities.objects.all().filter(active=True)
    context={'data':data}
    return render(request,'news/activities.html',context)


#تفاصيل الاخبار
def details(request,pk):
    news=News.objects.all().filter(id=pk)
    context={
        'news':news,
        }
    return render(request,'news/news_details.html',context)



#تفاصيل الاعلانات
def detailsAds(request,pk):
    ads=Ads.objects.all().filter(id=pk)
    context={
        'ads':ads,
        }
    return render(request,'news/ads_details.html',context)



#تفاصيل الانشطة
def detailsAct(request,pk):
    activities=Activities.objects.all().filter(id=pk)
    context={
        'activities':activities,
        }
    return render(request,'news/activities_details.html',context)


