from django.urls import path
from . import views

urlpatterns = [
    path('', views.pradinis, name='home'),
    path('perziura/', views.perziura, name='perziura'),
    path('registracija/', views.registracija, name='registracija'),
]