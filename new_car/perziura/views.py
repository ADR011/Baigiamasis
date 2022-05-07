from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from django.shortcuts import render
from .models import Order, Marke, Metai, Modelis, Spalva
from django.views.decorators.csrf import csrf_exempt



def perziura(request):
    klientai = Order.objects.all()
    context={'klientai': klientai}
    return render(request, 'perziura.html', context=context)

def pradinis(request):
#    return HttpResponse("Hello, world. You're at the registracija page.")
    return render(request, 'pradinis.html')

def registracija(request):
    if request.method=='POST':
        user_name = request.POST.get('user_name')
        user_last_name = request.POST.get('last_name')
        user_email = request.POST.get('email')
        marke = request.POST.get('marke')
        modelis = request.POST.get('modelis')
        metai = request.POST.get('metai')
        spalva = request.POST.get('spalva')
        new = Order(vardas = user_name, pavarde = user_last_name, email = user_email)
        new.save()
        marke = Marke(marke = marke)
        modelis = Modelis(modelis = modelis)
        metai = Metai(metai = metai)
        spalva = Spalva(spalva = spalva)
        marke.save()
        modelis.save()
        metai.save()
        spalva.save()
        modelis.metai.add(metai)
        marke.modelis.add(modelis)
        modelis.spalva.add(spalva)
        # new.marke.add(marke)
        # new.save() 
    listas = []
    modeliai = Modelis.objects.all()
    markes = Marke.objects.all()
    metai = Metai.objects.all()

    spalvos = Spalva.objects.all()
    for marke in markes:
        data = {}
        data['marke']=marke.marke
        data['modeliai'] = []

        for modelis in marke.modelis.all():
            naujas_modelis = {}
            naujas_modelis['modelis'] = modelis.modelis
            naujas_modelis['metai'] = []
            for m in modelis.metai.all():
                naujas_modelis['metai'].append(str(m.metai))
            data['modeliai'].append(naujas_modelis)
        listas.append(data)
    return render(request, 'registracija.html',context = {'listas':listas})


################################################################


@csrf_exempt
def load_modeliai(request):
    marke_id = request.POST.get('marke_id')

    modeliai = Modelis.objects.filter(marke__marke__contains = marke_id)
    return render(request, 'options_modelis.html', {'modeliai': modeliai})
    #return JsonResponse(list(modeliai.values('id', 'name')), safe=False)

@csrf_exempt
def load_spalvos(request):
    modelis_id = request.POST.get('modelis_id')
    print(modelis_id)
    spalvos = Spalva.objects.filter(modeliai__modelis__contains = modelis_id)
    print(spalvos)
    return render(request, 'options_spalvos.html', {'spalvos': spalvos})
    #return JsonResponse(list(modeliai.values('id', 'name')), safe=False)

@csrf_exempt
def load_metais(request):
    modelis_id = request.POST.get('modelis_id')
    print(modelis_id)
    metais = Metai.objects.filter(modeliai__modelis__contains = modelis_id)
    print(metais)
    return render(request, 'options_metai.html', {'metais': metais})
    


