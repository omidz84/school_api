from django.urls import path

from . import views


app_name = 'teacher'
urlpatterns = [
    path('register/', views.TeacherRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.TeacherProfileView.as_view(), name='profile'),
    path('class/add/student/<int:pk>/', views.ClassAddStudentView.as_view(), name='class-add-student'),
    path('news/add/', views.NewsView.as_view(), name='news-add'),
    path('practice/add/', views.PracticeView.as_view(), name='practice-add'),
    path('news/update/<int:pk>/', views.NewsUpdateView.as_view(), name='news-update'),
    path('practice/update/<int:pk>/', views.PracticeUpdateView.as_view(), name='practice-update'),
]
