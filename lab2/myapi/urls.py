from django.urls import path
from myapi import views

urlpatterns = [
    path('student/', views.student_list),
    path('student_details/<int:pk>/', views.student_detail),

]