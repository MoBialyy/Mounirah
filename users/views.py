from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login_users(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request,("There was an error loggin in, Please try again"))
            return redirect('login')
        
    else:
        return render(request,'userss/login.html',{'user':User.objects.all()})

def logout_users(request):
    logout(request)
    #messages.success(request,("You were logged out!"))
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            #messages.success(request,"Sign Up Successfully")
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request,'userss/signup.html',{'form':form},)