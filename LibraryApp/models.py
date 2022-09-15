from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your models here.
class customusers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first = models.CharField( max_length=50)
    last = models.CharField( max_length=50)
    
    


    
class Books(models.Model):
    title = models.CharField( max_length=50)
    author = models.CharField( max_length=50)
    category = models.CharField( max_length=50)
    price = models.DecimalField( max_digits=5, decimal_places=2)
