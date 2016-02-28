from django.contrib import admin
from .models import Student, Prof, Inscription

# Register your models here.

admin.site.register(Student)
admin.site.register(Prof)
admin.site.register(Inscription)
