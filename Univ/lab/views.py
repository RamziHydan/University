from django.shortcuts import render
from .models import *
# Create your views here.


#معمل كلية الهندسة
def engLab(request):
    data=EngineerLab.objects.all().filter(active=True)
    context={'data':data}
    return render(request,'univlab/engLab.html',context)



#معمل كلية الطب
def medLab(request):
    data=MedicineLab.objects.all().filter(active=True)
    context={'data':data}
    return render(request,'univlab/medLab.html',context)