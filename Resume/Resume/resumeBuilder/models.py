import email
from statistics import mode
from django.db import models

# Create your models here.
class Profile(models.Model):
    degree=models.CharField(max_length=100)
    university=models.CharField(max_length=100)

class user_profile(models.Model):
    firstname=models.CharField(max_length=100)
    lasttname=models.CharField(max_length=100)
    bod=models.DateField(max_length=8)
    password=models.CharField(max_length=100)
    emailid=models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    gender=models.CharField(max_length=30)

    def __str__(self):
        return self.firstname
