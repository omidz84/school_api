from django.urls import path

from . import views


app_name = 'teacher'
urlpatterns = [
    path('register/', views.TeacherRegisterView.as_view(), name='register'),
    path('login/', views.TeacherLoginView.as_view(), name='login'),
]
