from django.utils.translation import gettext as _
from rest_framework import status

from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from user.models import User
from school import models


class TeacherRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.TeacherRegisterSerializer


class TeacherProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.TeacherProfileSerializer


class ClassAddStudentView(UpdateAPIView):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassAddStudentSerializer

    def update(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg': _('student add to class.')}, status.HTTP_200_OK)
