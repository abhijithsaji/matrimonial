from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


class Customer(models.Model): 
    # Registration

    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20, choices = [('Male','male'),('Female','female'),('Other','other')],null=True)
    address = models.TextField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=13, null=True)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)
    uname = models.CharField(max_length=200,null=True)

    image = models.ImageField(upload_to='static/images/profile',default='static/images/user.png')

    def __str__(self):
        return self.name