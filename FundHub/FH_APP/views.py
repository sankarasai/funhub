from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request,'Home_Page/homepage.html')

def pricing(request):
    return render(request,'Nav-Content/pricing.html')

def pricing(request):
    return render(request,'Nav-Content/pricing.html')

def login_page(request):
    return render(request,'Nav-Content/login.html')

def login_check(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST['login_username']
        password = request.POST['login_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage') 
        else:
            messages.error(request, 'Bad Credentials. Please try again.')
    return render(request,'Nav-Content/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('homepage')  
        else:
            messages.error(request, 'User Name already Exists...')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('homepage')  

@login_required(login_url='/login_page')
def watch_content(request):
    return render(request,'Nav-Content/watch_content.html')

@login_required(login_url='/login_page')
def create_content(request):
    return render(request,'Nav-Content/create_content.html')


