from django.shortcuts import render
from .models import *
# Create your views here.
#الصفحة الرئيسية للكليات
def collage(request):
    
    return render(request,'collage/collage.html')





            #### كلية الطب  ####
# الصفحة الرئيسية لكلية الهندسة           
def medicine(request):
    data=Collage.objects.all().filter(active=True)
    context={'data':data,'major':major}
    return render(request,'collage/medicine/medicine.html',context)
#مكتبة الكلية
def collagelibm(request):
    return render(request,'collage/medicine/collagelib.html')
#تخصصات الكلية
def majorm(request):
    major=MedicineMajor.objects.all().filter(active=True)
    context={'data':major}
    return render(request,'collage/medicine/major.html',context)
#الاستراتيجية
def strategym(request):
    strategy=AdditionMessage.objects.all().filter(active=True)
    image=AdditonalImage.objects.all().filter(active=True)
    data=Collage.objects.all().filter(active=True)
    str=StrategyMed.objects.all().filter(active=True )
    # str=strategy_collage.filter(id=1)
    context={'data':data,'strategy':strategy,'image':image,'str':str}
    return render(request,'collage/medicine/strategy.html',context)
#الكادر
def teamm(request):
    data=CollageMedTeam.objects.all().filter(active=True)
    context={'data':data}
    return render(request,'collage/medicine/team.html',context)







            #### كلية الهندسة  ####
# الصفحة الرئيسية لكلية الخندسة           
def engineering(request):
    return render(request,'Collage/engineering/engineering.html')
#مكتبة الكلية
def collagelib(request):
    return render(request,'Collage/engineering/collagelib.html')
#تخصصات الكلية
def major(request):
    major=EngineerMajor.objects.all().filter(active=True)
    context={'major':major}
    return render(request,'Collage/engineering/major.html',context)
#الاستراتيجية
def strategy(request):
    strategy=AdditionMessage.objects.all().filter(active=True)
    image=AdditonalImage.objects.all().filter(active=True)
    data=Collage.objects.all().filter(active=True)
    str=StrategyEng.objects.all().filter(active=True )
    # str=strategy_collage.filter(id=1)
    context={'data':data,'strategy':strategy,'image':image,'str':str}
    return render(request,'Collage/engineering/strategy.html',context)
#الكادر
def team(request):  
    team=CollageEngTeam.objects.all().filter(active=True)
    count_t=team.filter(active=True).count()
    context={'team':team,'count_t':count_t}
    return render(request,'Collage/engineering/team.html',context)



            #### كلية العلوم  ####
# الصفحة الرئيسية لكلية الخندسة           
def humanities(request):
    return render(request,'Collage/humanities/humanty.html')
#مكتبة الكلية
def collhumlib(request):
    return render(request,'Collage/humanities/collagelib.html')
#تخصصات الكلية
def hmajor(request):
    major=HumanityMajor.objects.all().filter(active=True)
    context={'major':major}
    return render(request,'Collage/humanities/major.html',context)
#الاستراتيجية
def hstrategy(request):
    strategy=AdditionMessage.objects.all().filter(active=True)
    image=AdditonalImage.objects.all().filter(active=True)
    data=Collage.objects.all().filter(active=True)
    str=StrategyHum.objects.all().filter(active=True )
    # str=strategy_collage.filter(id=1)
    context={'data':data,'strategy':strategy,'image':image,'str':str}
    return render(request,'Collage/humanities/strategy.html',context)
#الكادر
def hteam(request):  
    team=CollageHumTeam.objects.all().filter(active=True)
    count_t=team.filter(active=True).count()
    context={'team':team,'count_t':count_t}
    return render(request,'Collage/humanities/team.html',context)


