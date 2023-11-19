from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from school_api.utils import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/school/', include('school.urls')),
    path('api/teacher/', include('teacher.urls')),
    path('api/user/', include('user.urls')),
    path('api/student/', include('student.urls')),

    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
