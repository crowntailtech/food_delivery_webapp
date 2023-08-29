from django.shortcuts import render
from partnerwithus.models import Partner_with_us
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.

#----------------------------------- Restaurant Registration ------------------------------#

def partner(request):
        if request.method =='POST':
                Restaurant_Name = request.POST.get('Restaurant_Name')
                fs = FileSystemStorage()
                request_file = request.FILES.get('aadhar_file')
                file = fs.save(request_file.name, request_file)
                aadhar_file=fs.url(file)
                Mobile_Number = request.POST.get('Mobile_Number')
                Email = request.POST.get('Email')
                City = 'Dehradun'
                fssai_num = request.POST.get('fssai_num')
                fssai_exp_date = request.POST.get('fssai_exp_date')
                own_name = request.POST.get('own_name')
                own_aadhar = request.POST.get('own_aadhar')
                own_address = request.POST.get('own_address')
                own_mobile = request.POST.get('own_mobile')
                gst_num = request.POST.get('gst_num')
                pan_num = request.POST.get('pan_num')
                acc_num = request.POST.get('acc_num')
                bank_name = request.POST.get('bank_name')
                branch_name = request.POST.get('branch_name')
                ifsc_code = request.POST.get('ifsc_code')
                request_file = request.FILES.get('gst_file')
                file = fs.save(request_file.name, request_file)
                gst_file=fs.url(file)
                request_file = request.FILES.get('pan_file')
                file = fs.save(request_file.name, request_file)
                pan_file=fs.url(file)
                request_file = request.FILES.get('sign_file')
                file = fs.save(request_file.name, request_file)
                sign_file=fs.url(file)
                request_file = request.FILES.get('img_file')
                file = fs.save(request_file.name, request_file)
                img_file=fs.url(file)
                request_file = request.FILES.get('menu_file') 
                file = fs.save(request_file.name, request_file)
                menu_file=fs.url(file)
                partner_info = Partner_with_us(Restaurant_Name=Restaurant_Name,Mobile_Number=Mobile_Number,Email=Email,City=City,
                fssai_num=fssai_num,fssai_exp_date=fssai_exp_date,own_name=own_name,own_aadhar =own_aadhar,own_address =own_address,
                own_mobile=own_mobile,gst_num =gst_num ,pan_num =pan_num,acc_num=acc_num,bank_name=bank_name,branch_name =branch_name ,
                ifsc_code= ifsc_code,aadhar_file=aadhar_file,gst_file=gst_file,pan_file=pan_file,sign_file=sign_file,img_file=img_file,menu_file=menu_file)
                partner_info.save()
                messages.success(request,'Your details has been submitted successfully... Stay Tunned!')
                return render(request,'restaurantpartner.html')
        else:
                return render(request,'restaurantpartner.html')



#------------------------------------------------------------------------ End ------------------------------------------------------------#