from django.contrib import admin
from structure.models import Programme
from .models import CareerOption,Facualty
from users.models import Teacher,Student

app_name= 'structure'

class ProgrammeInLine(admin.TabularInline):
    model = Programme
    

class CareerOptionInLine(admin.TabularInline):
    model = CareerOption

class Teacherinline(admin.TabularInline):
    model =Teacher


class FacualtyLines(admin.ModelAdmin):
    inlines= [ProgrammeInLine]

class ProgrammeLines(admin.ModelAdmin):
    inlines =[CareerOptionInLine]



admin.site.register(Facualty,FacualtyLines)
admin.site.register(Programme,ProgrammeLines)
admin.site.register(Teacher)
admin.site.register(Student)







