from django.shortcuts import render, redirect

# Create your views here.
from .models import Student
def createstudent(request):
    context = {}
    context['ID'] = 1
    if (request.method == 'GET'):
        return render(request, 'createstudent.html',context)
    else:
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        Student.objects.create(name=name, username=username, email=email)
        student = Student.objects.all()
        context['student'] = student
        context['msg'] = 'student inserted'
        return redirect("home")


