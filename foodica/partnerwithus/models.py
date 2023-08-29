from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField

# Create your models here.

#--------------------------------------- Restaurant Data Table ----------------------------------#

class Partner_with_us(models.Model):
    Restaurant_Name = models.CharField(max_length=255,null=True)
    Mobile_Number = models.IntegerField()
    Email = models.EmailField(unique=True)
    City = models.CharField(max_length=15,null=True)
    fssai_num = models.CharField(max_length=255, null=True)
    fssai_exp_date=models.DateField(null=True)
    own_name = models.CharField(max_length=50,null=True)
    own_aadhar = models.IntegerField(null=True)
    aadhar_file=models.FileField(upload_to='media/', null=True)
    own_address = models.CharField(max_length=250,null=True)
    own_mobile = models.IntegerField(null=True)
    gst_num = CharField(max_length=255, null=True)
    gst_file=models.FileField(upload_to='media/', null=True)
    pan_num = CharField(max_length=255, null=True)
    acc_num = models.IntegerField(null=True)
    bank_name = models.CharField(max_length=50,null=True)
    branch_name = models.CharField(max_length=100,null=True)
    ifsc_code = models.CharField(max_length=100,null=True)
    pan_file=models.FileField(upload_to='media/', null=True)
    sign_file=models.FileField(upload_to='media/', null=True)
    img_file=models.FileField(upload_to='media/', null=True)
    menu_file=models.FileField(upload_to='media/', null=True)

    #----------------------------------------------------------- End -----------------------------------------------------#