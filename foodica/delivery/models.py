from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#------------------------------ Delivery Boy Data Table ---------------------------------#
class Delivery(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.IntegerField(max_length=12)
    alternate_contact = models.IntegerField(max_length=12)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField(null=True)
    address = models.TextField(max_length=255)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    nationality = models.CharField(max_length=25)
    pincode = models.IntegerField(max_length=6)
    identity = models.CharField(max_length=10)
    vehicle = models.CharField(max_length=10)
    driving_license = models.CharField(null=True, max_length=255)
    privacy_policy = models.BooleanField(null=True)


#-------------------------------------------------------------------- End -----------------------------------------------------#    