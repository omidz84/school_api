from django.urls import path

from . import views


app_name = 'school'
urlpatterns = [
    path('', views.SchoolView.as_view(), name='get-post'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('course/', views.CourseView.as_view(), name='course-get-post'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('class/', views.ClassView.as_view(), name='class-get-post'),
    path('class/<int:pk>/', views.ClassDetailView.as_view(), name='class-detail'),
]
