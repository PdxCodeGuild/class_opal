from django.contrib import admin

# Register your models here.
# import everything
from .models import *
# register your Student class in models
admin.site.register(Student)