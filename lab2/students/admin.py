from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Student, Track

# Register your models here.
admin.site.register(Student)
admin.site.register(Track)
