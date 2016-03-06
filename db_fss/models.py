from __future__ import unicode_literals

from django.db import models

from re import search,compile

from djano.core.exceptions import ValidationError


# Create your models here.

class Student(models.Model):
    cin = models.CharField(max_length=8)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephonne = models.CharField(max_length=12, blank=True) 
    mail = models.EmailField()
    
    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)
    
    def clean(self):

        mcin=r'^(([a-zA-Z][a-zA-Z0-9])|([0-9]){2})[0-9]{6}$'
        mcinc=compile(mcin)
	
        if mcinc.search(self.cin) is None:
            raise ValidationError("identificateur cin non valide!")

	
	mtel=r'^[0-9]{8}$'
        mtelc=compile(mtel)

       if mtelc.search(self.telephonne) is None:
           raise ValidationError("numéro de téléphone non valide!")


       
     



            
        

        
	

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
