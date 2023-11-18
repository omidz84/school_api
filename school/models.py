from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.gis.db import models as model

from rest_framework.validators import ValidationError

from user.models import User
from .validators import validate_file_extension

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=350, unique=True, db_index=True, verbose_name=_('School name'))
    address = models.TextField(verbose_name=_('School address'))
    location = model.GeometryField(geography=True, verbose_name=_('Location'))

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=350, unique=True, db_index=True, verbose_name=_('Course name'))

    def __str__(self):
        return self.name


class Class(models.Model):
    school = models.ForeignKey(to=School, on_delete=models.CASCADE, verbose_name=_('school'))
    teacher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='teacher', verbose_name=_('teacher'))
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name=_('course'))
    students = models.ManyToManyField(to=User, related_name='students', verbose_name=_('students'))

    def __str__(self):
        return f'{self.school.name} | {self.teacher.username} | {self.course.name}'


class News(models.Model):
    title = models.CharField(max_length=500, db_index=True, verbose_name=_('Title'))
    body = models.TextField(verbose_name=_('body'))
    class_id = models.ForeignKey(to=Class, on_delete=models.CASCADE, verbose_name=_('class'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return f'{self.title} | {self.class_id.__str__()}'


class Practice(models.Model):
    title = models.CharField(max_length=500, db_index=True, verbose_name=_('Title'))
    body = models.TextField(verbose_name=_('body'))
    file = models.FileField(upload_to='Practice/', validators=[validate_file_extension], null=True, blank=True, verbose_name=_('file'))
    class_id = models.ForeignKey(to=Class, on_delete=models.CASCADE, verbose_name=_('class'))
    Submission_deadline = models.DateField(verbose_name=_('Submission deadline'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return f'{self.title} | {self.class_id.__str__()}'


class PracticeResponse(models.Model):
    body = models.TextField(verbose_name=_('body'))
    file = models.FileField(upload_to='Practice/response/', validators=[validate_file_extension], null=True, blank=True, verbose_name=_('file'))
    practice = models.ForeignKey(to=Practice, on_delete=models.CASCADE, verbose_name=_('practice'))
    student = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_('student'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return f'{self.student.username} | {self.practice.__str__()}'

    def save(self, *args, **kwargs):
        dat_now = timezone.now().day
        day_Submission_deadline = self.practice.Submission_deadline.day
        month_now = timezone.now().month
        month_Submission_deadline = self.practice.Submission_deadline.month
        if dat_now > day_Submission_deadline or month_now > month_Submission_deadline:
            raise ValidationError(_('The time for sending the practice has ended.'))
        return super().save(*args, **kwargs)
