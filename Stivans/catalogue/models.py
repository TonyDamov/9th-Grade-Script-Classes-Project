from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import CustomUser


# Create your models here.

class Item(models.Model):
    rating = models.DecimalField(validators=[MinValueValidator(1), MaxValueValidator(5)], max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='products', default='default.png')
    name = models.CharField(max_length=256)
    description =models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)




class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)