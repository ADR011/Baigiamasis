from django.urls import path
from . import views

urlpatterns = [
    # path('', views.pradinis, name='home'),
    # path('perziura/', views.perziura, name='perziura'),
    # path('registracija/', views.registracija, name='registracija'),
    


    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),


    path('ajax/load-modeliai/', views.load_modeliai, name='ajax_load_modeliai'), # AJAX
]