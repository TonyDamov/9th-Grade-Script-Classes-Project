from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Street(models.Model) :
    name = models.CharField(max_length=128)
    number = models.IntegerField()

class Address(models.Model) :
    street = models.ForeignKey('Street', on_delete=models.PROTECT)
    province = models.CharField(max_length=256)
    municipality = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=64)

class CustomUser(models.Model) :
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    address = models.ForeignKey('Address', on_delete=models.PROTECT)


    
# Create your models here.
