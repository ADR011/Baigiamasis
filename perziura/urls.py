from django.urls import path
from . import views

urlpatterns = [
    path('', views.Perziura.as_view(), name='pradinis'),
    path('perziura/', views.Perziura.as_view(), name='perziura'),
    path('registracija/', views.Registracija.as_view(), name='registracija'),
    # path('ivykdyti/', views.Ivykdyti.as_view(), name='ivykdyti'),
    path('ivykdyti/', views.klientas_list_done, name='ivykdyti'),

    path('<int:pk>/', views.Redagavimas.as_view(), name='redagavimas'),
    path('pasalinimas/<int:pk>/', views.Pasalinimas.as_view(), name='pasalinimas'),


    path('ajax/load-modeliai/', views.load_modeliai, name='ajax_load_modeliai'),
    path('ajax/load-spalvos/', views.load_spalvos, name='ajax_load_spalvos'),
    path('ajax/load-metais/', views.load_metais, name='ajax_load_metais'),
]