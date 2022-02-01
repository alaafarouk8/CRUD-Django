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

def searchstudent(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        students = Student.objects.all().filter(username=username)
        if students:
            context = {'search_students': students}
            return render(request, 'createstudent.html', context)
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def deletestudent(request, id):
    sturecord = Student.objects.get(id=id)
    if sturecord:
        sturecord.delete()
        student = Student.objects.all()
        context = {'students': student}
        return render(request, 'createstudent.html', context)
    else:
        return render(request, 'home.html')
def liststudent(request):
    student = Student.objects.all()
    context = {'students': student}
    return render(request, 'liststudent.html', context)



def updatestudent(request,id):
    if request.method == 'POST':
        username = request.POST.get('username')
        student = Student.objects.get(id=id)
        if student:
            student.username = username
            student.save()
            students = Student.objects.all()
            context = {'students': students}
            return render(request, 'createstudent.html', context)
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')

