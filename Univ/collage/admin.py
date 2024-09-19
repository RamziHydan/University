from django.contrib import admin
from .models import *
# from univinfo import models
# Register your models here.
admin.site.register(Collage)
admin.site.register(MedicineMajor)
admin.site.register(EngineerMajor)
admin.site.register(AdditionMessage)
admin.site.register(AdditonalImage)
admin.site.register(StrategyMed)
admin.site.register(StrategyEng)
admin.site.register(CollageEngTeam)
admin.site.register(HumanityMajor)
admin.site.register(CollageHumTeam)

class CollageMedAdmin(admin.ModelAdmin):
    list_filter=['date_created','active']
    list_display=['name','job','email','phone','active','image','facebook']
    list_display_links=['image']
    list_editable=['name','job','email','phone','active','facebook']
    search_fields=['name','job']
admin.site.register(CollageMedTeam,CollageMedAdmin)



admin.site.site_header=' جامعة دار السلام الدولية'
admin.site.site_title='Univ'
# admin.site.register(Major)
