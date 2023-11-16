from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'teacher', 'course']


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'class_id', 'created_at', 'updated_at']


@admin.register(models.Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'class_id', 'Submission_deadline']


@admin.register(models.PracticeResponse)
class PracticeResponseAdmin(admin.ModelAdmin):
    list_display = ['id', 'practice', 'student']
