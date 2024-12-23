from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=20)
    time = models.DecimalField(decimal_places=1, max_digits=3)
    description = models.TextField()
    body = models.TextField()
    author = models.CharField(max_length=20)
    img = models.ImageField()
    

