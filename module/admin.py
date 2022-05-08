from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline
from django.db import models
from users.models import Teacher

from .models import Module,Chapter, Objective,Section,Concept

class ChapterInLine(admin.TabularInline):
    model = Chapter

class ObjectiveInLine(admin.TabularInline):
    model = Objective

class ModuleLines(admin.ModelAdmin):
    inlines = [ObjectiveInLine]

admin.site.register(Module,ModuleLines)




class SectionInLine(admin.TabularInline):
    model = Section

class ChapterLines(admin.ModelAdmin):
    inlines = [SectionInLine]

admin.site.register(Chapter,ChapterLines)



class ConceptInLine(admin.TabularInline):
    model = Concept

class SectionLines(admin.ModelAdmin):
    inlines = [ConceptInLine]

admin.site.register(Section,SectionLines)


admin.site.register(Concept)
admin.site.register(Objective)
