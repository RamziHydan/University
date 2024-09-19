from . models import Student
from django import forms

class StudentForm(forms.ModelForm):
    # name=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"text",
            
    #         "placeholder":"الاسم",
    #     }),label="")
    # emission_date=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"form-control",
    #         "type":"date",
    #     }),label="تاريخ الاصدار")
    # date_created=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"form-control",
    #         "type":"date",
    #     }))
    # birth_date=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"form-control",
    #         "type":"date",
    #     }),label='تاريخ الميلاد')
    # certification_date=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"form-control",
    #         "type":"date",
    #     }),label='تاريخ الشهادة')
    # nationality=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":"الجنسية",
    #     }),label="")
    # birth_place=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":"مكان الميلاد",
    #     }),label="")
   
    # rate=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":"المعدل",
    #     }),label="")
    # certification_place=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":" مكان  الحصول عليها",
    #     }),label="")
    # governor=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":"المحافظة",
    #     }),label="")
    # school=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":"اسم المدرسة",
    #     }),label=" ")
    # emission_place=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":" مكان الاصدار  ",
    #     }),label=" ")
    # phone=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"number",            
    #         "placeholder":"رقم هاتف الطالب",
    #     }),label=" ")
    # address=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":"العنوان",
    #     }),label="")
    # email=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"text",            
    #         "placeholder":"البريد",
    #     }),label="")
    # reationship=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"",            
    #         "placeholder":"ولي الامر",
    #     }),label=" ")
    # his_phone=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"number",            
    #         "placeholder":"  رقم هاتف ولي الامر",
    #     }),label=" ")
    # card_number=forms.CharField(widget=forms.TextInput(attrs={
    #         "class":"",
    #         "type":"number",            
    #         "placeholder":"رقم الهوية",
    #     }),label="")
    class Meta:
        model=Student        
        fields='__all__'