from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from . import serializers, models


class SchoolView(ListCreateAPIView):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer


class SchoolDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer


class CourseView(ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class ClassView(ListCreateAPIView):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer


class ClassDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer

