from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
import jwt
from datetime import datetime, timedelta
from django.conf import settings

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, role=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')

        email = self.normalize_email(email)
        if not role: role = self.model.GUEST

        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, role, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email=email, password=password, role=role, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER = 0
    SPEACIALIST = 1
    ADMIN = 2
    GUEST = 3

    ROLE_CHOICES = (
        (USER, 'User'),
        (SPEACIALIST, 'Specialist'),
        (ADMIN, 'Admin')
    )


    email = models.EmailField(verbose_name='email', unique=True)
    login = models.CharField(verbose_name='login', max_length=40, unique=True)
    role = models.PositiveSmallIntegerField(verbose_name='role',
                                            choices=ROLE_CHOICES, default=GUEST)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'login']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(CustomUser, self).save(*args, **kwargs)
        return self