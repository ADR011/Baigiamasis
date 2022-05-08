from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonForm
from .models import Klientas, Marke, Modelis
# , Metai, Spalva
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView
from multiprocessing import context
from .models import Klientas, Marke, Modelis, Metai, Spalva
from django.urls import reverse_lazy




# def perziura(request):
#     klientai = Order.objects.all()
#     context={'klientai': klientai}
#     return render(request, 'perziura.html', context=context)

def pradinis(request):
    return render(request, 'pradinis.html')

# def registracija(request):
#     if request.method=='POST':
#         user_name = request.POST.get('user_name')
#         user_last_name = request.POST.get('last_name')
#         user_email = request.POST.get('email')
#         marke = request.POST.get('marke')
#         modelis = request.POST.get('modelis')
#         metai = request.POST.get('metai')
#         spalva = request.POST.get('spalva')
#         new = Order(vardas = user_name, pavarde = user_last_name, email = user_email)
#         new.save()
#         marke = Marke(marke = marke)
#         modelis = Modelis(modelis = modelis)
#         metai = Metai(metai = metai)
#         spalva = Spalva(spalva = spalva)
#         marke.save()
#         modelis.save()
#         metai.save()
#         spalva.save()
#         modelis.metai.add(metai)
#         marke.modelis.add(modelis)
#         modelis.spalva.add(spalva)
#         # new.marke.add(marke)
#         # new.save() 
#     listas = []
#     modeliai = Modelis.objects.all()
#     markes = Marke.objects.all()
#     metai = Metai.objects.all()

#     spalvos = Spalva.objects.all()
#     for marke in markes:
#         data = {}
#         data['marke']=marke.marke
#         data['modeliai'] = []

#         for modelis in marke.modelis.all():
#             naujas_modelis = {}
#             naujas_modelis['modelis'] = modelis.modelis
#             naujas_modelis['metai'] = []
#             for m in modelis.metai.all():
#                 naujas_modelis['metai'].append(str(m.metai))
#             data['modeliai'].append(naujas_modelis)
#         listas.append(data)
#     # print(metai)
#     return render(request, 'registracija.html',context = {'listas':listas})


################################################################

class Perziura(ListView):
    model = Klientas
    context_object_name = 'klientai'

class Registracija(CreateView):
    model = Klientas
    form_class = PersonForm
    # fields = ('klientas_vardas', 'klientas_pavarde', 'klientas_email', 'klientas_spalva')
    success_url = reverse_lazy('pradinis')


class Redagavimas(UpdateView):
    model = Klientas
    form_class = PersonForm
    # fields = ('klientas_vardas', 'klientas_pavarde', 'klientas_email', 'klientas_spalva')
    success_url = reverse_lazy('perziura')





@csrf_exempt
def load_modeliai(request):
    marke_id = request.POST.get('marke_id')
    # print('marke_id', marke_id)
    # modeliai = Modelis.objects.filter(marke__marke__contains = marke_id)
    modeliai = Modelis.objects.filter(marke_id=marke_id).all()
    print('modelis', modeliai)
    return render(request, 'options_modelis.html', {'modeliai': modeliai})
#  def load_modeliai(request):
#     marke_id = request.POST.get('marke_id')
#     modeliai = Modelis.objects.filter(marke__marke__contains = marke_id)
#     return render(request, 'options_modelis.html', {'modeliai': modeliai})


@csrf_exempt
def load_metais(request):
    modelis_id = request.POST.get('modelis_id')
    metais = Modelis.objects.filter(modelis_id=modelis_id).all()
    print('metai', metais)
    return render(request, 'options_metai.html', {'metais': metais})


@csrf_exempt
def load_spalvos(request):
    modelis_id = request.POST.get('modelis_id')
    spalvos = Modelis.objects.filter(modelis_id=modelis_id).all()
    print('spalvos', spalvos)
    return render(request, 'options_spalvos.html', {'spalvos': spalvos})
    #return JsonResponse(list(modeliai.values('id', 'name')), safe=False)


    


