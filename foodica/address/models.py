from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Custaddress(models.Model):
    phone_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_complete_address = models.CharField(max_length=255)
    user_floor = models.CharField(max_length=255)
    user_how_to_reach = models.CharField(max_length=255)
    user_address_type=models.CharField(max_length=255)
