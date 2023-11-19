from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext as _

from .validators import check_phone, isnumeric


# Create your models here.


class MyUserManager(UserManager):
    """
        Creating a new user manager for our customized django user.
    """

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('first_name', 'admin')
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        db_index=True,
        unique=True,
        validators=[check_phone],
        verbose_name=_('phone number')
    )
    code_meli = models.CharField(
        max_length=10,
        db_index=True,
        unique=True,
        validators=[isnumeric],
        verbose_name=_('code meli')
    )
    objects = MyUserManager()

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name} | {self.phone_number}'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
