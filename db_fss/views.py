from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Student, Prof, Inscription

def home(request):
    return render(request, 'db_fss/home.html')

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class ProfList(ListView):
    model = Prof
