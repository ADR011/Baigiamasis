from tkinter import TRUE
from django.db import models
import datetime

# Create your models here.
class Order(models.Model):
    vardas = models.CharField('vardas', max_length=10)
    pavarde = models.CharField('pavarde', max_length=20)
    gimimo_data = models.CharField('gimimo data', max_length=20)
    email = models.CharField('email', max_length=30)
    class Meta:
        verbose_name = 'Uzsakymas'
        verbose_name_plural = 'Uzsakymai'

    def __str__(self):
        return self.vardas   

class Marke(models.Model):
    automobilio_marke = models.CharField('automobilio marke', max_length=20, null=True, blank=True, default='pass')
    orders = models.ManyToManyField(Order, null=True, related_name='marke', blank=True)
    class Meta:
        verbose_name = 'Marke'
        verbose_name_plural = 'Markes'

    def __str__(self):
        return self.automobilio_marke  

class Modelis(models.Model):
    automobilio_modelis = models.CharField('automobilio modelis', max_length=20, null=True, blank=True, default='pass')
    markes = models.ForeignKey(Marke, on_delete=models.DO_NOTHING, null=True, related_name='modelis')
    class Meta:
        verbose_name = 'Modelis'
        verbose_name_plural = 'Modeliai'

    def __str__(self):
        return self.automobilio_modelis 

class Metai(models.Model): 
    automobilio_pagaminimo_metai = models.DateField('automobilio pagaminimo metai', null=True, blank=True, default=datetime.date.today)
    modeliai = models.ForeignKey(Modelis, on_delete=models.DO_NOTHING, null=True, related_name='metai')
    class Meta:
        verbose_name = 'Metai'
        verbose_name_plural = 'Metai'

    def __str__(self):
        return f'{self.automobilio_pagaminimo_metai}' 

