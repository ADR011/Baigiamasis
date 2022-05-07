from tkinter import Pack
from django.db import models

from tkinter import TRUE
from django.db import models
import datetime

# Create your models here.
class Order(models.Model):
    vardas = models.CharField('vardas', max_length=10, blank=True, null=True)
    pavarde = models.CharField('pavarde', max_length=20, blank=True, null=True)
    email = models.CharField('email', max_length=30, blank=True, null=True)
    gimimo_data = models.CharField(max_length=124, blank=True, null=True)

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
        return str(self.marke)  

class Modelis(models.Model):
    modelis = models.CharField('automobilio modelis', max_length=20, null=True, blank=True, default='pass')
    marke = models.ForeignKey(Marke, on_delete=models.CASCADE, null=True, related_name='modelis')
    class Meta:
        verbose_name = 'Modelis'
        verbose_name_plural = 'Modeliai'

    def __str__(self):
        return str(self.modelis) 


class Metai(models.Model): 
    metai = models.DateField('automobilio pagaminimo metai', max_length=20, null=True, blank=True, default=datetime.date(2022,3,1))
    modeliai = models.ForeignKey(Modelis, on_delete=models.CASCADE, null=True, related_name='metai')
    class Meta:
        verbose_name = 'Metai'
        verbose_name_plural = 'Metais'

    def __str__(self):
        # return str(self.metai)
        return '{}'.format(self.metai)

class Spalva(models.Model): 
    spalva = models.CharField(max_length=124, blank=True, null=True)
    modeliai = models.ForeignKey(Modelis, on_delete=models.CASCADE, null=True, related_name='spalva')
    class Meta:
        verbose_name = 'Spalva'
        verbose_name_plural = 'Spalva'

    def __str__(self):
        return str(self.spalva)



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


# class Klientas(models.Model):

#     Vardas = models.CharField(max_length=124)
#     Pavardė = models.CharField(max_length=124)
#     El_pastas = models.CharField(max_length=124)
#     Gimimo_metai = models.CharField(max_length=124)

#     klientas_vardas = models.CharField('kliento vardas', max_length=124, blank=False, null=True)
#     klientas_pavarde = models.CharField('kliento pavarde', max_length=124, blank=False, null=True)
#     klientas_email = models.CharField('email', max_length=30, blank=True, null=True)
#     klientas_spalva = models.CharField('Automobilio spalva', max_length=15, blank=True, null=True)


#     marke = models.ForeignKey(Marke, on_delete=models.SET_NULL, blank=True, null=True)
#     modelis = models.ForeignKey(Modelis, on_delete=models.SET_NULL, blank=True, null=True)


#     def __str__(self):
#         # return self.klientas_vardas, self.klientas_pavarde
#         return '{} {} {} {}'.format(self.klientas_vardas, self.klientas_pavarde, self.klientas_email, self.klientas_spalva)



# class Metai(models.Model): 
#     metai = models.DateField('automobilio pagaminimo metai', null=True, blank=True, default=datetime.date.today)
#     modeliai = models.ForeignKey(Modelis, on_delete=models.DO_NOTHING, null=True, related_name='metai')
#     class Meta:
#         verbose_name = 'Metai'
#         verbose_name_plural = 'Metai'

#     def __str__(self):
#         return '{}'.format(self.metai)

