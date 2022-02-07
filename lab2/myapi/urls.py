from django.urls import path
from myapi import views

urlpatterns = [
    # path('student/', views.student_list),
   # path('student_details/<int:pk>/', views.student_detail),
    path('student/', views.StudentAPI.as_view()),
    path('student_details/<int:id>/', views.Student_DetailsAPI.as_view()),

]