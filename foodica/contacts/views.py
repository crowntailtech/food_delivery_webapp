from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from contacts.models import Complaint, Contacts
from contacts.models import Feedback

# Create your views here.

#------------------------ Contact Us Part----------------------------#

def contactus(request):
    if request.method =='POST':
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_message=request.POST.get('msg')    
        user_contacts=User.objects.create_user(user_name,user_email,user_message)  
        contact_us = Contacts(user_name=user_name, user_email=user_email, user_message=user_message, created_by=user_contacts)      
        contact_us.save()
        print("Success")
        messages.success(request,'We will contact you soon. Thank you')
        return render(request,'contactus.html')
    else:
        return render(request,'contactus.html')

#--------------------------  Feedback Part ----------------------------#

def aboutus(request):
    if request.method =='POST':
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_message=request.POST.get('msg')       
        feedback_us = Feedback(user_name=user_name, user_email=user_email, user_message=user_message, created_by=user_feedback)      
        feedback_us.save()
        print("Success")
        messages.success(request,'Thank you')
        return render(request,'aboutus.html')
    else:
        return render(request,'aboutus.html')

#-------------------------- Complaints Part ----------------------------#    
#    
def complaint(request):
    if request.method =='POST':
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_city=request.POST.get('city')
        user_message=request.POST.get('complaint_msg')   
        user_feedback=User.objects.create_user(user_name,user_email,user_message)    
        feedback_us = Complaint(user_name=user_name, user_email=user_email, user_city=user_city, user_message=user_message, created_by=user_feedback)      
        feedback_us.save()
        print("Success")
        messages.success(request,'Thank you')
        return render(request,'aboutus.html')
    else:
        return render(request,'comp.html')

#---------------------------------------------------------- End --------------------------------------------------------------------------#