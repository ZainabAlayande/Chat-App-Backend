import datetime
from typing import Any
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.context_processors import auth
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class BioData(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=4, default="0000")

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        db_table = 'chatapp_user'

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} {self.username}"


class Customer(AbstractUser):
    bio_data = models.OneToOneField(BioData, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True, default='default')
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    last_seen = models.DateTimeField(null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customer_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
