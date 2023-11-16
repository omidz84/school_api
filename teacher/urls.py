from django.urls import path

from . import views


app_name = 'teacher'
urlpatterns = [
    path('register/', views.TeacherRegisterView.as_view(), name='register'),
    path('class/add/student/<int:pk>/', views.ClassAddStudentView.as_view(), name='class-add-student'),
]
