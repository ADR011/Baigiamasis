from django.urls import path
from . import views

urlpatterns = [
    path('', views.pradinis, name='home'),
    path('perziura/', views.perziura, name='perziura'),
    path('registracija/', views.registracija, name='registracija'),
    


    path('ajax/load-modeliai/', views.load_modeliai, name='ajax_load_modeliai'), # AJAX
    path('ajax/load-spalvos/', views.load_spalvos, name='ajax_load_spalvos'), # AJAX
    path('ajax/load-metais/', views.load_metais, name='ajax_load_metais'), # AJAX
]