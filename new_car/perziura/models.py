# from tkinter import Pack
# from django.db import models

# from tkinter import TRUE
# import datetime

# # Create your models here.
# class Order(models.Model):
#     vardas = models.CharField('vardas', max_length=10, blank=True, null=True)
#     pavarde = models.CharField('pavarde', max_length=20, blank=True, null=True)
#     email = models.CharField('email', max_length=30, blank=True, null=True)
#     gimimo_data = models.CharField(max_length=124, blank=True, null=True)

#     class Meta:
#         verbose_name = 'Uzsakymas'
#         verbose_name_plural = 'Uzsakymai'

#     def __str__(self):
#         return self.vardas   

# class Marke(models.Model):
#     marke = models.CharField('automobilio marke', max_length=20, null=True, blank=True, default='pass')
#     orders = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='marke', blank=True,)
#     class Meta:
#         verbose_name = 'Marke'
#         verbose_name_plural = 'Markes'

#     def __str__(self):
#         return str(self.marke)  

# class Modelis(models.Model):
#     modelis = models.CharField('automobilio modelis', max_length=20, null=True, blank=True, default='pass')
#     marke = models.ForeignKey(Marke, on_delete=models.CASCADE, null=True, related_name='modelis')
#     class Meta:
#         verbose_name = 'Modelis'
#         verbose_name_plural = 'Modeliai'

#     def __str__(self):
#         return str(self.modelis) 


# class Metai(models.Model): 
#     metai = models.DateField(null=True, blank=True)
#     modeliai = models.ForeignKey(Modelis, on_delete=models.CASCADE, null=True, related_name='metai')
#     class Meta:
#         verbose_name = 'Metai'
#         verbose_name_plural = 'Metais'

#     def __str__(self):
#         return '{}'.format(self.metai)


# class Spalva(models.Model): 
#     spalva = models.CharField(max_length=124, blank=True, null=True)
#     modeliai = models.ForeignKey(Modelis, on_delete=models.SET_DEFAULT, default=None, null=True, related_name='spalva')
#     class Meta:
#         verbose_name = 'Spalva'
#         verbose_name_plural = 'Spalva'

#     def __str__(self):
#         return str(self.spalva)



from django.db import models

from tkinter import TRUE
from django.db import models
import datetime


class Marke(models.Model):
    marke = models.CharField(max_length=20, null=True, blank=True, default='mark')
    # orders = models.ManyToManyField(Order, null=True, related_name='marke', blank=True)
    # class Meta:
    #     verbose_name = 'Marke'
    #     verbose_name_plural = 'Markes'

    def __str__(self):
        return self.marke  

class Modelis(models.Model):
    modelis = models.CharField('automobilio modelis', max_length=20, null=True, blank=True, default='pass')
    marke = models.ForeignKey(Marke, on_delete=models.CASCADE, null=True)
    # class Meta:
    #     verbose_name = 'Modelis'
    #     verbose_name_plural = 'Modeliai'

    def __str__(self):
        return self.modelis 


class Metai(models.Model):
    metai = models.CharField('metai', max_length=20, null=True, blank=True, default='None')
    modelis = models.ForeignKey(Modelis, on_delete=models.DO_NOTHING, null=True)
    def __str__(self):
        return self.metai 


class Spalva(models.Model):
    spalva = models.CharField('spalva', max_length=20, null=True, blank=True, default='None')
    modelis = models.ForeignKey(Modelis, on_delete=models.DO_NOTHING, null=True)
    def __str__(self):
        return self.spalva 


class Klientas(models.Model):
    klientas_vardas = models.CharField(max_length=124, blank=False, null=True)
    klientas_pavarde = models.CharField(max_length=124, blank=False, null=True)
    klientas_email = models.CharField(max_length=30, blank=True, null=True)
    marke = models.ForeignKey(Marke, on_delete=models.SET_NULL, null=True)
    modelis = models.ForeignKey(Modelis, on_delete=models.SET_NULL, null=True)
    metai = models.ForeignKey(Metai, on_delete=models.SET_NULL, null=True)
    spalva = models.ForeignKey(Spalva, on_delete=models.SET_NULL, null=True)



    # marke = models.ForeignKey(Marke, on_delete=models.SET_NULL, blank=True, null=True)
    # modelis = models.ForeignKey(Modelis, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        # return self.klientas_vardas, self.klientas_pavarde
        # return '{} {} {} {}'.format(self.klientas_vardas, self.klientas_pavarde, self.klientas_email, self.klientas_spalva)
        return self.klientas_vardas
