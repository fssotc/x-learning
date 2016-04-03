from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Student, Prof, Inscription, Matiere


def home(request):
    return render(request, 'db_fss/home.html')


class StudentList(ListView):
    model = Student


class StudentDetail(DetailView):
    model = Student


class ProfList(ListView):
    model = Prof


class ProfDetail(DetailView):
    model = Prof


class MatiereList(ListView):
    module = Matiere

    def get_queryset(self):
        """return Matiere"""
        return Matiere.objects.order_by('-nom')[:5]
