from django.shortcuts import render
from .models import *
# Create your views here.
from django.utils.translation import get_language,activate,gettext

# البيئة الجامية
def env(request):
    trans=translate(language='ar')

    build=BuildingInfo.objects.all().filter(active=True)
    context={'build':build,'trans':trans}
    return render(request,'univlife/univenv.html',context)


def translate(language):
    cur_lang=get_language()
    try:
        activate(language)
    finally:
        activate(cur_lang)
#اوائل الطلاب
def perfect(request):
    student=PerfectStu.objects.all().filter(active=True)
    context={'student':student}
    return render(request,'univlife/perfectstu.html',context)


#مرافق خدمية
def services(request):
    return render(request,'univlife/servicesection.html')

#ارشاد طلاب اكاديمي
def guide(request):
    return render(request,'univlife/studentguide.html')







#تفاصيل البيئة الجامعة
def detailsEnv(request,pk):
    build=BuildingInfo.objects.all().filter(id=pk)
    context={
        'build':build
        }
    return render(request,'univlife/env_details.html',context)


#تفاصيل الطلاب    
def detailsStu(request,pk):
    student=PerfectStu.objects.all().filter(id=pk)
    context={
        'student':student
        }
    return render(request,'univlife/stu_details.html',context)