from django.urls import path

from . import views


app_name = 'student'
urlpatterns = [
    path('register/', views.StudentRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', views.StudentProfileView.as_view(), name='register'),
    path('class/', views.StudentClassView.as_view(), name='class'),
    path('news/', views.StudentNewsView.as_view(), name='news'),
    path('news/<int:pk>/', views.DetailNewsView.as_view(), name='detail-news'),
    path('practice/', views.StudentPracticeView.as_view(), name='practice'),
    path('practice/<int:pk>/', views.DetailPracticeView.as_view(), name='detail-practice'),
    path('practice/response/', views.StudentPracticeResponseView.as_view(), name='practice-response'),
    path('practice/response/<int:pk>/', views.DetailStudentPracticeResponseView.as_view(), name='detail-practice-response'),
]
