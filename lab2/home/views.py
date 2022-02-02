from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import myUser
from django.contrib.auth import authenticate, login as authlogin
# Create your views here.
from django.utils.datastructures import MultiValueDict


def register(request):
    if (request.method == 'GET'):
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myUser.objects.create(username=username, email=email, password=password)
        User.objects.create_user(username, email, password, is_staff=True)
        return redirect("login")


def about(request):
    return render(request, 'about.html')


def liststudent(request):
    return render(request, 'liststudent.html')


def home(request):
    return render(request, 'home.html')

def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    elif(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        print(email, "  Password ", password)
        try:
            user = myUser.objects.get(email=email, password=password)
            admin_user = authenticate(username=user.username, password=password)
            if user and admin_user is not None:
                request.session['username'] = user.username
                authlogin(request, admin_user)
                return redirect('home')
        except myUser.DoesNotExist:
            return redirect("login")


def contact(request):
    return render(request, 'contact.html')


def logout(request):
    request.session.clear()
    return redirect("login")
