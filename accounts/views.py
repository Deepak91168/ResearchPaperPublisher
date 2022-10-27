from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == "POST":
        FName = request.POST['firstName']
        LName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if (User.objects.filter(username=username).exists()):
                print("User Already exists")
                messages.info(request,'User Already exists')
                return redirect('/accounts/register')
            elif (User.objects.filter(email=email).exists()):
                print("Email Already in use")
                messages.info(request,'Email Already in use')
                return redirect('/accounts/register')
            else:
                # Working Well
                user = User.objects.create_user(username=username,
                                                password=password,
                                                email=email,first_name=FName,last_name=LName)
                user.save()
                print("User Registered")
                return redirect('/')
        else:
            print("Password not equal to cpassword")
            messages.info(request,'Password not equal to cpassword')
            return redirect('/accounts/register')
    else:
        return render(request, 'turnup/register.html')
