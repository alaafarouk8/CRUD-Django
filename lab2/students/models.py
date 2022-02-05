from django.db import models


# Create your models here.
class Track(models.Model):
    id = models.AutoField(primary_key=True)
    trackname = models.CharField(max_length=50)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    trackid = models.ForeignKey('Track', on_delete=models.CASCADE, blank=True, null=True)


class Intake(models.Model):  # ORM
    name = models.CharField(max_length=30,blank=True, null=True)


class Trainee(models.Model):
    fullname = models.CharField(max_length=40)

