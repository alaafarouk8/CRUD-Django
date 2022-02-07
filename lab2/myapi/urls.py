from django.urls import path
from myapi import views
from myapi.serializers import Studentserializers
from students.models import Student

urlpatterns = [
    # path('student/', views.student_list),
   # path('student_details/<int:pk>/', views.student_detail),
    path('student/', views.StudentAPI.as_view()),
    path('student_details/<int:id>/', views.Student_DetailsAPI.as_view()),
path('generic/', views.GenericStudentAPI.as_view(queryset=Student.objects.all(), serializer_class=Studentserializers), name='student-list')

]