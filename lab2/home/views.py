from django.shortcuts import render, redirect
from .models import Intake


# Create your views here.
from django.utils.datastructures import MultiValueDict

def register(request):
    if (request.method == 'GET'):
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Intake.objects.create(username=username, email=email, password=password)
        return redirect("login")
def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:
        email = request.POST.get('email', "")
        password = request.POST.get('password', "")
        print(email, "  Password ", password)
        intakes = Intake.objects.all()
        print({intakes})
        for intake in intakes:
            if intake.email == email and intake.password == password:
                return redirect("home")
            else:
                return redirect("login")


def contact(request):
    return render(request, 'contact.html')
