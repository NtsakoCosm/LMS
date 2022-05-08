from django.contrib import admin
from .models import Choice, Quiz,Question

class QuestionInline(admin.TabularInline):

    model = Question

class QuizLines(admin.ModelAdmin):
    inlines = [QuestionInline]

class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionLines(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Quiz,QuizLines)

admin.site.register(Question,QuestionLines)


# Register your models here.
