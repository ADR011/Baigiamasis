from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from multiprocessing import context
from .models import Klientas, Marke, Modelis, Metai, Spalva
from django.urls import reverse_lazy



def pradinis(request):
    return render(request, 'perziura/pradinis.html')

# ################################################################
# class Ivykdyti(ListView):
#     model = Klientas
#     context_object_name = 'klientai'




# def ivykdyti(request):
#    listas = Klientas.objects.all()
#    return render(request, 'perziura/klientas_list_done.html', {'listas' : listas})

  
def klientas_list_done(request):
    klientai = Klientas.objects.all()
    context={'klientai': klientai}
    return render(request, 'perziura/klientas_list_done.html', context=context)



class Perziura(ListView):
    model = Klientas
    context_object_name = 'klientai'


# class Ivykdyti(ListView):
#     model = Klientas
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context_object_name = 'klientai'
#         return context
  

class Registracija(CreateView):
    model = Klientas
    form_class = PersonForm
    # fields = ('klientas_vardas', 'klientas_pavarde', 'klientas_email', 'klientas_spalva')
    success_url = reverse_lazy('perziura')


class Redagavimas(UpdateView):
    model = Klientas
    form_class = PersonForm
    # fields = ('klientas_vardas', 'klientas_pavarde', 'klientas_email', 'klientas_spalva')
    success_url = reverse_lazy('perziura')

class Pasalinimas(DeleteView):
    model = Klientas
    # form_class = PersonForm
    # fields = ('klientas_vardas', 'klientas_pavarde', 'klientas_email', 'klientas_spalva')
    success_url = reverse_lazy('perziura')



@csrf_exempt
def load_modeliai(request):
    marke_id = request.POST.get('marke_id')
    # print('marke_id', marke_id)
    # modeliai = Modelis.objects.filter(marke__marke__contains = marke_id).all()
    modeliai = Modelis.objects.filter(marke_id=marke_id).all()
    print('modeliai', modeliai)
    return render(request, 'perziura/options_modelis.html', {'modeliai': modeliai})
    #  def load_modeliai(request):
#     marke_id = request.POST.get('marke_id')
#     modeliai = Modelis.objects.filter(marke__marke__contains = marke_id)
#     return render(request, 'options_modelis.html', {'modeliai': modeliai})




@csrf_exempt
def load_metais(request):
    modelis_id = request.POST.get('modelis_id')
    # metais = Metai.objects.filter(modelis__modelis__contains = modelis_id)
    # modeliai = Modelis.objects.filter(ivykdytas=False).all()
    metais = Metai.objects.filter(modelis_id=modelis_id).all()
    print('metais', metais)
    return render(request, 'perziura/options_metai.html', {'metais': metais})



@csrf_exempt
def load_spalvos(request):
    modelis_id = request.POST.get('modelis_id')
    # modeliai = Modelis.objects.filter(ivykdytas=False).all()
    # spalvos = Spalva.objects.filter(modelis__modelis__contains = modelis_id)
    spalvos = Spalva.objects.filter(modelis_id=modelis_id).all()
    print('spalvos', spalvos)
    return render(request, 'perziura/options_spalvos.html', {'spalvos': spalvos})
    #return JsonResponse(list(modeliai.values('id', 'name')), safe=False)
    

