from django.contrib import admin
from .models import Student, Prof, Inscription, Semestre, Module, Matiere

# Register your models here.

admin.site.register(Student)
admin.site.register(Prof)
admin.site.register(Inscription)
admin.site.register(Matiere)
admin.site.register(Module)
admin.site.register(Semestre)


