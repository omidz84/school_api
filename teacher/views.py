from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from user.models import User


class TeacherRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.TeacherRegisterSerializer


class TeacherLoginView(GenericAPIView):
    serializer_class = serializers.TeacherLoginSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
