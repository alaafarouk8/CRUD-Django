from django import forms

from students.models import Student, Trainee, Intake


class AddStudent(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)


class AddStudent1(forms.ModelForm):
    class Meta:
        fields = '__all__'  # ['username','name','email',trackid]#'__all__'
        model = Student

class Traineeinsert(forms.Form):
    fullname = forms.CharField(label='Name',max_length=30,widget=forms.Textarea)
    bdate = forms.DateField(label='Birth Date')

class Traineeinsert1(forms.ModelForm):
   class Meta:
       fields='__all__'#['fullname','trackid']#'__all__'
       model=Trainee
