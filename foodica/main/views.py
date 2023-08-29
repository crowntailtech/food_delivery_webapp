from django.contrib.auth import login
from django.shortcuts import redirect, render
from accounts.views import*
from partnerwithus import views

# Create your views here.


def helpp(request):
    return render(request,'help.html')
def home(request):
    print("Develpoed By Aditya Kumar")
    return render(request,'index.html')
def term(request):
    return render(request,'term.html')
def delivery(request):
        return render(request,"delivery.html")
def partnerwithus(request):
    return render(request,'partnerwithus.html')
# def services(request):
#     return redirect(partnerwithus)
def error(request):
    return render(request,'error.html')



