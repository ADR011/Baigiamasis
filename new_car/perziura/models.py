from django.db import models

from tkinter import TRUE
from django.db import models
import datetime

# Create your models here.
class Order(models.Model):
    vardas = models.CharField('vardas', max_length=10)
    pavarde = models.CharField('pavarde', max_length=20)
    email = models.CharField('email', max_length=30)

    class Meta:
        verbose_name = 'Uzsakymas'
        verbose_name_plural = 'Uzsakymai'

    def __str__(self):
        return self.vardas   

class Marke(models.Model):
    marke = models.CharField('automobilio marke', max_length=20, null=True, blank=True, default='pass')
    orders = models.ManyToManyField(Order, null=True, related_name='marke', blank=True)
    class Meta:
        verbose_name = 'Marke'
        verbose_name_plural = 'Markes'

    def __str__(self):
        return self.marke  

class Modelis(models.Model):
    modelis = models.CharField('automobilio modelis', max_length=20, null=True, blank=True, default='pass')
    marke = models.ForeignKey(Marke, on_delete=models.CASCADE, null=True, related_name='modelis')
    class Meta:
        verbose_name = 'Modelis'
        verbose_name_plural = 'Modeliai'

    def __str__(self):
        return self.modelis 


class Metai(models.Model): 
    metai = models.DateField('automobilio pagaminimo metai', max_length=20, null=True, blank=True, default=datetime.date.today)
    modeliai = models.ForeignKey(Modelis, on_delete=models.DO_NOTHING, null=True, related_name='metai')
    class Meta:
        verbose_name = 'Metai'
        verbose_name_plural = 'Metai'

    def __str__(self):
        return self.metai


##############################################################################
# class Marke(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Modelis(models.Model):
#     name = models.CharField(max_length=40)
#     marke = models.ForeignKey(Marke, on_delete=models.CASCADE)
    

#     def __str__(self):
#         return self.name


class Klientas(models.Model):
    klientas_vardas = models.CharField('kliento vardas', max_length=124, blank=False, null=True)
    klientas_pavarde = models.CharField('kliento pavarde', max_length=124, blank=False, null=True)
    klientas_email = models.CharField('email', max_length=30, blank=True, null=True)
    klientas_spalva = models.CharField('Automobilio spalva', max_length=15, blank=True, null=True)

    marke = models.ForeignKey(Marke, on_delete=models.SET_NULL, blank=True, null=True)
    modelis = models.ForeignKey(Modelis, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        # return self.klientas_vardas, self.klientas_pavarde
        return '{} {} {} {}'.format(self.klientas_vardas, self.klientas_pavarde, self.klientas_email, self.klientas_spalva)


class Metai(models.Model): 
    metai = models.DateField('automobilio pagaminimo metai', null=True, blank=True, default=datetime.date.today)
    modeliai = models.ForeignKey(Modelis, on_delete=models.DO_NOTHING, null=True, related_name='metai')
    class Meta:
        verbose_name = 'Metai'
        verbose_name_plural = 'Metai'

    def __str__(self):
        return '{}'.format(self.metai)
