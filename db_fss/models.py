from __future__ import unicode_literals

from django.db import models

from re import search,compile

from djano.core.exceptions import ValidationError


# Create your models here.

class Student(models.Model):
    cin = models.CharField(max_length=8,primary_key=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephonne = models.CharField(max_length=12, blank=True)
    email = models.EmailField()

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
    cin = models.CharField(primary_key=True,max_length=8)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=12, blank=True)
    adresse = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "%s %s" % (self.nom, self.prenom)
    
    	




class Inscription(models.Model):
    num = models.PositiveIntegerField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.num)
        
class Matiere(models.Model):
	nom = models.CharField(max_length=200)
	coff = models.FloatField()
	cours = models.BooleanField()
	td = models.BooleanField()
	tp = models.BooleanField()
	nb_heure = models.DecimalField(max_digits=4,decimal_places=2)
	
	def __str__(self):
		return self.nom
    
        
        
class Module(models.Model):
	nom = models.CharField(max_length=200)
	coff = models.FloatField()
	matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
	m_type = models.CharField(max_length=200)

class Semestre(models.Model):
	num = models.PositiveIntegerField()
	module = models.ForeignKey(Module, on_delete=models.CASCADE)



class News(models.Model):
	titre = models.CharField(max_length=20)
	contenu = models.TextField()
	n_date = models.DateField(auto_now=False,auto_now_add=True)
	author=models.ForeignKey(Prof,on_delete=models.CASCADE)

class Club(models.Model):
	nom = models.CharField(max_length=20)
	description = models.CharField(max_length=2000)
	email = models.CharField(max_length=30)

class Departement(models.Model):
	nom = models.CharField(max_length=30)
	chefdep = models.ForeignKey(Prof,on_delete=models.CASCADE)



class Specialite(models.Model):
	nom = models.CharField(max_length=30)
	nbstudent = models.PositiveSmallIntegerField()
	dept=models.ForeignKey( Departement,on_delete=models.CASCADE)
	etudiant = models.ForeignKey(Student,on_delete=models.CASCADE)


class Outil(models.Model):
	nom = models.CharField(max_length=20)
	description = models.CharField(max_length=2000)
	version = models.FloatField()
# db for the most useful urls
class Lien(models.Model):
	l_lien = models.CharField(max_length=20)
