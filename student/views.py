from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

from . import serializers
from user.models import User


class StudentRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.StudentRegisterSerializer


class StudentProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.StudentProfileSerializer

