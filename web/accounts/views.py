from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def login(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if username == '' or password1 == '' or password1=='':
            messages.info(request,'Need to enter all details')
            return redirect('register')

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already exists')
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request,'email alreadt exists')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name , email = email, username = username, password = password1)
                user.save()
                messages.info(request,'user created successfully')
                return redirect('login')

        else:
            print('password not matching....')

        return redirect('/')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
