import email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == "POST":
        FName = request.POST['firstName']
        LName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=FName,
                                        last_name=LName)
        user.save()
        print("User Registered")
        return redirect('/')
    else:
        return render(request, 'turnup/register.html')
