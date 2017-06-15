from django.contrib import admin

from .models import Exam, Question


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3


class ExamAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title']})]
    inlines = [QuestionInline]


admin.site.register(Exam, ExamAdmin)
