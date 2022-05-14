from django.db import models

from tkinter import TRUE
from django.db import models
import datetime


class Marke(models.Model):
    marke = models.CharField(max_length=20, null=True, blank=True, default='marke')
    def __str__(self):
        # return self.marke  
        return '{}'.format(self.marke) 
                           

class Modelis(models.Model):
    modelis = models.CharField(max_length=20, null=True, blank=True, default='modelis')
    marke = models.ForeignKey(Marke, on_delete=models.CASCADE, null=True)
    def __str__(self):
        # return self.modelis 
        return '{}'.format(self.modelis)
      

class Metai(models.Model):
    metai = models.CharField(max_length=20, null=True, blank=True, default='metai')
    modelis = models.ForeignKey(Modelis, on_delete=models.CASCADE, null=True)
    def __str__(self):
        # return self.metai 
        return '{}'.format(self.metai)

      
class Spalva(models.Model):
    spalva = models.CharField(max_length=20, null=True, blank=True, default='spalva')
    modelis = models.ForeignKey(Modelis, on_delete=models.CASCADE, null=True)
    def __str__(self):
        # return self.spalva 
        return '{}'.format(self.spalva)


class Klientas(models.Model):
    ivykdytas = models.BooleanField(verbose_name="ivykdytas", default=False)
    klientas_vardas = models.CharField(max_length=124, blank=True, null=True)
    klientas_pavarde = models.CharField(max_length=124, blank=True, null=True)
    klientas_email = models.CharField(max_length=30, blank=True, null=True)
    marke = models.ForeignKey(Marke, on_delete=models.SET_NULL, null=True)
    modelis = models.ForeignKey(Modelis, on_delete=models.SET_NULL, null=True)
    metai = models.ForeignKey(Metai, on_delete=models.SET_NULL, null=True)
    spalva = models.ForeignKey(Spalva, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        # return self.klientas_vardas
        return '{}'.format(self.klientas_vardas)