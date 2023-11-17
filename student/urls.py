from django.urls import path

from . import views


app_name = 'student'
urlpatterns = [
    path('register/', views.StudentRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.StudentProfileView.as_view(), name='register'),
    path('class/', views.StudentClassView.as_view(), name='class'),
]
