import delivery
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from delivery.models import Delivery
import sqlite3

# Create your views here.


#--------------------- Register Delivey Boy Itself ------------------#

def deliveryboy(request):
    if request.method =='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        contact_no2 = request.POST.get('contact_no2')
        gender=request.POST.get('gender')
        birthdate=request.POST.get('birthday')
        address = request.POST.get('address')
        state=request.POST.get('state')
        city=request.POST.get('city')
        nationality=request.POST.get('nationality')
        pincode=request.POST.get('pincode')
        identity=request.POST.get('identity')
        vehicle = request.POST.get('vehicle')
        driving_license_no = request.POST.get('driving_license_no')
        termsandcondition=request.POST.get('flexRadioDefault')
        if termsandcondition is not None:
            terms=True
            # user_delivery=User.objects.create_user(user_first_name,user_last_name,user_email,user_contact,user_alt_contact,user_age)  
            user_delivery = Delivery(first_name=first_name,last_name=last_name,email=email,contact=contact_no,alternate_contact=contact_no2,gender=gender,birthdate=birthdate,
                                    address=address,state=state,city=city,nationality=nationality,pincode=pincode,
                                    identity=identity,vehicle=vehicle,driving_license=driving_license_no,privacy_policy=terms)
            user_delivery.save();
            print("Success")

            messages.success(request,'Your details has been submitted sucessfully.')
            return render(request,'newform.html')
        else:
            messages.success(request,'Please accept privacy policy.')
            return render(request,'newform.html')
    else:
        return render(request,'newform.html')


#-------------------------------------------------------------- End ----------------------------------------------------------#