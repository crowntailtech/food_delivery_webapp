from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#-------------------- Contactus Table ----------------------#
class Contacts(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_message = models.CharField(max_length=255)
    created_by = models.OneToOneField(User,unique=False, related_name='contacts', on_delete=models.CASCADE)

#-------------------- Feedback Table ----------------------#   
class Feedback(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_message = models.CharField(max_length=255)
    created_by = models.OneToOneField(User,unique=False, related_name='feedback', on_delete=models.CASCADE)

#-------------------- Complaint Table ----------------------#

class Complaint(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_city = models.CharField(max_length=255)
    user_message = models.CharField(max_length=255)
    created_by = models.OneToOneField(User,unique=False, related_name='complaint', on_delete=models.CASCADE)


    #------------------------------------------------------------ End -------------------------------------------------------#