from django.shortcuts import render
from .models import *
# Create your views here.





#الرؤية والرسالة
def vision(request):
    vision=VisionMessage.objects.all().filter(active='True')
    addition_message=AdditionMessage.objects.all().filter(active='True')
    addition_image=AdditonalImage.objects.all().filter(active='True')
    context={'data':vision,'add':addition_message,'photo':addition_image}
    return render(request,'UnivInfo/vision.html',context)


#سيرة رئيس مجلس الامناء
def boardpre(request):
    board_CV=BoardPresident.objects.all().filter(active='True')
    addition_message=AdditionMessage.objects.all().filter(active='True')
    addition_image=AdditonalImage.objects.all().filter(active='True')
    context={'data':board_CV,'add':addition_message,'photo':addition_image}

    return render(request,'UnivInfo/boardpreCV.html',context)

#كلمة رئيس الجامع
def univpre(request):
    Pre_word=UnivPresidentWord.objects.all().filter(active='True')
    addition_message=AdditionMessage.objects.all().filter(active='True')
    addition_image=AdditonalImage.objects.all().filter(active='True')
    context={'data':Pre_word,'add':addition_message,'photo':addition_image}
    return render(request,'UnivInfo/univpreWord.html',context)

#كادر الجامعة
def univteam(request):
    teamdata=UnivTeam.objects.all().filter(active='True')
    context={'data':teamdata}
    return render(request,'UnivInfo/univteam.html',context)




#تفاصيل البيئة الجامعة
def detailsTem(request,pk):
    team=UnivTeam.objects.all().filter(id=pk)
    context={
        'team':team
        }
    return render(request,'UnivInfo/tem_details.html',context)

