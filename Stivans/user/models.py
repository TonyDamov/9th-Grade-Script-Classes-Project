from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUser(AbstractUser):
    street_name = models.CharField(max_length=128)
    street_number = models.IntegerField()
    province = models.CharField(max_length=256)
    municipality = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=64)
