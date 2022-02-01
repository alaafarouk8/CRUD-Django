from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
import students
from .models import Student


def createstudent(request):
    context = {}
    context['ID'] = 1
    if (request.method == 'GET'):
        return render(request, 'createstudent.html', context)
    else:
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        Student.objects.create(name=name, username=username, email=email)
        student = Student.objects.all()
        context = {'students': student}
        return render(request, 'createstudent.html', context)

def deletestudent(request,id):
    sturecord = Student.objects.get(id=id)
    if sturecord:
        sturecord.delete()
        student = Student.objects.all()
        context = {'students': student}
        return render(request, 'createstudent.html', context)
    else:
        return Http404('there is no student')
