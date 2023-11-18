from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from user.permissions import CustomModelPermissions
from . import serializers, models


class SchoolView(ListCreateAPIView):
    permission_classes = [CustomModelPermissions]
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer


class SchoolDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
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

