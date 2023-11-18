from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from . import serializers
from user.models import User
from school import models


class StudentRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.StudentRegisterSerializer


class StudentProfileView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.StudentProfileSerializer


class StudentClassView(GenericAPIView):
    serializer_class = serializers.StudentClassSerializer

    def get(self, request: Request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            decoded_token = AccessToken(token)
            user = User.objects.get(id=decoded_token["user_id"])
            Class = models.Class.objects.filter(students=user)
            s_class = self.serializer_class(instance=Class, many=True)
            return Response(s_class.data, status.HTTP_200_OK)
        except:
            return Response({'msg': 'Token invalid'}, status.HTTP_400_BAD_REQUEST)


class StudentNewsView(GenericAPIView):
    serializer_class = serializers.StudentNewsSerializer

    def get(self, request: Request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            decoded_token = AccessToken(token)
            user = User.objects.get(id=decoded_token["user_id"])
            Class = models.Class.objects.filter(students=user)
            news = models.News.objects.filter(class_id__in=Class)
            s_news = self.serializer_class(instance=news, many=True)
            return Response(s_news.data, status.HTTP_200_OK)
        except:
            return Response({'msg': 'Token invalid'}, status.HTTP_400_BAD_REQUEST)
