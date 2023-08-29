from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from address.models import Custaddress
from django.contrib.auth.models import User
from accounts.views import UsersViews
user_views = UsersViews()

# Create your views here.
#------------------------------ Adding Address by User --------------------------#
def Add_address(request):
    if request.method =='POST':
        user_complete_address=request.POST.get('complete address')
        user_floor=request.POST.get('floor')
        user_how_to_reach=request.POST.get('how to reach') 
        user_address_type=request.POST.get('type')
        user_add_address=User.objects.create_user(user_complete_address,user_floor,user_how_to_reach,user_address_type) 
        user_address = Custaddress(user_complete_address=user_complete_address, user_floor=user_floor, user_how_to_reach=user_how_to_reach,user_address_type=user_address_type)
        user_address.save()
        print("success")
        messages.success(request,'Your address has been added successfully')
        return redirect(user_views.user_profile)
    else:
        return redirect(user_views.user_profile)

#--------------------- Showing Address ---------------------------------#

def Show_address(request):  
    print("Show_address function is running")
    email=request.POST.get('email')
    address1 = Custaddress.objects.all(email=email)
    return render(request,'myprofile.html',{'address2':address1})