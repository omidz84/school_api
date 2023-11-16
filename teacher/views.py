from rest_framework.generics import CreateAPIView

from . import serializers
from user.models import User


class TeacherRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.TeacherRegisterSerializer
