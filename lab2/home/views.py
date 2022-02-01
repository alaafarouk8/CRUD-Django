from django.shortcuts import render, redirect
from .models import myUser


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
    else:
        email = request.POST['email']
        password = request.POST['password']
        print(email, "  Password ", password)

        is_user_exist = myUser.objects.all().filter(email=email, password=password)
        if is_user_exist:
            return redirect("home")
        else:
            return redirect("login")


def contact(request):
    return render(request, 'contact.html')
