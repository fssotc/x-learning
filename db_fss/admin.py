from django.contrib import admin
from .models import Student, Prof, Inscription, Semestre, Module, Matiere, Departement, News

# Register your models here.

admin.site.register(Student)
admin.site.register(Prof)
admin.site.register(Inscription)
admin.site.register(Matiere)
admin.site.register(News)
admin.site.register(Module)
admin.site.register(Semestre)
admin.site.register(Departement)
