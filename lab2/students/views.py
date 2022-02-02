from django.shortcuts import render
# Create your views here.
from django.views import View
from django.views.decorators.http import require_GET
from django.views.generic import FormView, CreateView, ListView

from .forms import *
from .models import Track


class insertStudentformmodelclass(View):
    def get(self, request):
        print('class based get')
        context = {}
        form = AddStudent1()
        context['GUI'] = form
        return render(request, 'createstudent.html', context)

    def post(self, request):
        print('class based post')
        context = {}
        afterpostform = AddStudent1(request.POST)
        afterpostform.save()
        student = Student.objects.all()
        context = {'students': student}
        return render(request, 'liststudent.html', context)


# Create your views here.z
@require_GET
def insertStudennformmodel(request):
    context = {}
    form = AddStudent1()
    if (request.method == 'GET'):
        context['GUI'] = form
        return render(request, 'createtrainee.html', context)
    else:
        afterpostform = AddStudent1(request.POST)
        afterpostform.save()
        student = Student.objects.all()
        context = {'students': student}
        return render(request, 'liststudent.html', context)


class TrackCreateView(CreateView):
    model = Track
    fields = '__all__'

class TrackList(ListView):
    model = Track

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


def updatestudent(request, id):
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
