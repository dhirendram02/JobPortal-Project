from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
class JobForm(models.Model):
    name = models.CharField(max_length=122)
    gender= models.CharField(max_length=200)
    Email = models.EmailField(default = None)
    phone = models.CharField(max_length=12)
    JobType = models.CharField(max_length=111)
    JobRole = models.CharField(max_length=122)
    Location = models.CharField(max_length=122)
    date = models.DateField()
    
class signin(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=20)
   
    def __str__(self):
        return self.Email
    