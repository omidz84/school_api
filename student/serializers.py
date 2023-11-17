from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.models import Group

from rest_framework import serializers

from user.models import User
from user.utils import get_tokens
from user.serializers import GroupSerializer
from school import models


class StudentRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8, label=_('confirm password'), write_only=True, required=True)
    groups = GroupSerializer(many=True, read_only=True)
    token = serializers.SerializerMethodField(read_only=True, label=_('token'))

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'code_meli',
            'password',
            'password2',
            'groups',
            'token',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'read_only': True},
        }

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise ValidationError(_('The passwords must match'))
        return data

    def get_token(self, obj):
        user = User.objects.get(id=obj.id)
        token = get_tokens(user)
        refresh = token['refresh']
        access = token['access']
        settings.REDIS_JWT_TOKEN.set(name=refresh, value=refresh, ex=settings.REDIS_REFRESH_TIME)
        return {'access': access, 'refresh': refresh}

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            code_meli=validated_data['code_meli'],
            password=validated_data['password'],
        )
        group = Group.objects.get(name='دانش‌ آموز')
        group.user_set.add(user)
        return user


class StudentProfileSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'code_meli',
            'groups',
        ]

