from django.contrib import admin

# Register your models here.
from trainee.models import Trainee, Track

admin.site.register(Trainee)
admin.site.register(Track)