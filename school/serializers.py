from rest_framework import serializers

from . import models


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = '__all__'
