from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    cin = models.CharField(max_length=8)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephonne = models.CharField(max_length=12, blank=True)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)

class Prof(models.Model):
    cin = models.CharField(max_length=8)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=12, blank=True)
    adresse = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)

class Inscription(models.Model):
    num = models.PositiveIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.num

class Semestre(models.Model):
	num = models.PositiveIntegerField()
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	
class Module(models.Model):
	nom = models.CharField(max_length=200)
	coff = models.FloatField()
	matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
	m_type = models.CharField(max_length=200)

class Matiere(models.Model):
	nom = models.CharField(max_length=200)
	coff = models.FloatField()
	cours = models.BooleanField()
	td = models.BooleanField()
	tp = models.BooleanField()
	nb_heure = models.PositiveIntegerField()

class News(models.Model):
	titre = models.CharField(max_length=20)
	n_url = models.CharField(max_length=100)
	n_date = models.DateField(auto_now=False,auto_now_add=True)
	author = models.CharField(max_length=200)

class Club(models.Model):
	nom = models.CharField(max_length=20)
	description = models.CharField(max_length=2000)
	email = models.CharField(max_length=30)

class Departement(models.Model):
	nom = models.CharField(max_length=30)
	chef_dep = models.CharField(max_length=30)
	nb_student = models.PosiviteIntegerField()

class Salle(models.Model):
	nom = models.CharField(max_length=20)
	capaciter = models.PositiveIntegerField() #capaciter de chaque salle
	
class Specialite(models.Model):
	nom = models.CharField(max_length=5)

class emploi(models.Model):
	specialite = models.ForeignKey(specialite)
	
	
