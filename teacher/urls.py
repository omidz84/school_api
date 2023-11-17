from django.urls import path

from . import views


app_name = 'teacher'
urlpatterns = [
    path('register/', views.TeacherRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.TeacherProfileView.as_view(), name='profile'),
    path('class/add/student/<int:pk>/', views.ClassAddStudentView.as_view(), name='class-add-student'),
]
