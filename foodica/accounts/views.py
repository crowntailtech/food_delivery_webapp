from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from address.models import Custaddress

from django.contrib.auth.models import User

# Create your views here.

class UsersViews:
    @staticmethod
    def register(request):
        if request.method == 'POST':
            full_name = request.POST['name']
            username = request.POST['phone']
            useremail = request.POST['email']
            upassword = request.POST['password']
            
            user = User.objects.create_user(
                username=username,
                first_name=full_name,
                password=upassword,
                email=useremail
            )
            
            messages.success(request, 'Your account has been created successfully')
            return redirect('login')
        else:
            return render(request, 'signup.html')

    @staticmethod
    def user_login(request):
        if request.method == 'POST':
            phone = request.POST['phone']
            password = request.POST['password']

            user = authenticate(username=phone, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('login')
        else:
            return render(request, 'login.html')

    @staticmethod
    @login_required(login_url='login')
    def user_profile(request):
        
        user = request.user
        print(user)
        #    addresses = Custaddress.objects.filter(phone_id=user)
        address1 = Custaddress.objects.filter(phone_id=user)
        
        context = {
            'Name': user.first_name,
            'email': user.email,
            'password': user.password,
            'phone': user.username,
            'address2': address1
        }
        
        return render(request, 'myprofile.html', context)

    @staticmethod
    @login_required
    def user_logout(request):
        logout(request)
        messages.success(request, 'You have logged out successfully!!')
        return redirect('home')

    @login_required
    def update_profile(request):
        if request.method == 'POST':
            email = request.user.email
            phone = request.POST['phone']
            name = request.POST['Name']
            
            user = User.objects.get(email=email)
            user.username = phone
            user.first_name = name

            new_pas = request.POST.get('new_psw')
            confirm_pas = request.POST.get('confirm_new_psw')
            
            if new_pas:  # If the user provided a new password
                current_pas = request.POST.get('current_psw')
                
                if current_pas and user.check_password(current_pas) and new_pas == confirm_pas:
                    user.set_password(new_pas)
                    messages.success(request, 'Your password has been changed successfully')
                elif current_pas and (not user.check_password(current_pas) or new_pas != confirm_pas):
                    messages.error(request, 'Password verification failed or new passwords do not match. Please try again.')

            user.save()

            messages.success(request, 'Your profile has been updated successfully')
            
            return redirect('myprofile')

        return redirect('myprofile')