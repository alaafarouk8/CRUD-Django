from django.db import models


# Create your models here.

class Student (models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
