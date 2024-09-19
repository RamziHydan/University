from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
from django.utils.translation import get_language,activate,gettext



def studentLogin(request):
    trans=translate(language='ar')
    form=StudentForm()
    if request.method=='POST':
        data=StudentForm(request.POST)
        if data.is_valid():
            data.save()                        
        else:
            data=StudentForm()          
        
    context={'data':form,'trans':trans}
    return render(request,'studentaff/login.html',context)




def schedule(request):
    # data=Schedule.objects.all().filter(active=True)
    context={}
    return render(request,'studentaff/schedule.html',context)

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Document
from django.http import HttpResponse
from django.shortcuts import get_object_or_404



def download(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    response = HttpResponse(document.document, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.document.name}"'
    return response





from django.views.generic import ListView

class DocumentListView(ListView):
    model = Document
    template_name = 'studentaff/documents.html'
    context_object_name = 'documents'




def translate(language):
    cur_lang=get_language()
    try:
        activate(language)
    finally:
        activate(cur_lang)
