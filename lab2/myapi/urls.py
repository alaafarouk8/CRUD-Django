from django.urls import path, include
from rest_framework import routers

from myapi import views
from myapi.serializers import Studentserializers
from myapi.views import StudentViewSet
from students.models import Student

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('studentlist/', views.student_list),
    path('student_details1/<int:pk>/', views.student_detail),
    path('student/', views.StudentAPI.as_view()),
    path('student_details/<int:id>/', views.Student_DetailsAPI.as_view()),
    path('generic/', views.GenericStudentAPI.as_view()),
   # path('student_details_generic/<int:id>/', views.GenericStudentdetailsAPI.as_view()),
    path('', include(router.urls)),
]
