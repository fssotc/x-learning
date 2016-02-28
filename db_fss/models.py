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
