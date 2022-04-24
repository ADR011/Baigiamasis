from multiprocessing import context
from django.shortcuts import render
from .models import Order, Marke, Metai, Modelis
from django.http import HttpResponse
def perziura(request):
    orders = Order.objects.all()
    context={'orders': orders}
    print(orders)
    return render(request, 'perziura.html', context=context)
def pradinis(request):
#    return HttpResponse("Hello, world. You're at the registracija page.")
    return render(request, 'pradinis.html')
def registracija(request):
    if request.method=='POST':
        user_name = request.POST.get('user_name')
        user_last_name = request.POST.get('last_name')
        user_date = request.POST.get('date')
        user_email = request.POST.get('email')
        user_marke = request.POST.get('marke')
        user_modelis = request.POST.get('modelis')
        user_metai = request.POST.get('metai')
        new = Order(vardas = user_name, pavarde = user_last_name, gimimo_data = user_date, email = user_email)
        new.save()
        marke = Marke(automobilio_marke = user_marke)
        modelis = Modelis(automobilio_modelis = user_modelis)
        metai = Metai(automobilio_pagaminimo_metai = user_metai)
        marke.save()
        modelis.save()
        metai.save()
        modelis.metai.add(metai)
        marke.modelis.add(modelis)
        new.marke.add(marke)
        new.save() 
    listas = []
    modeliai = Modelis.objects.all()
    markes = Marke.objects.all()
    metai = Metai.objects.all()
    for marke in markes:
        data = {}
        # print(marke.modelis.all())
        data['marke']=marke.automobilio_marke
        data['modeliai'] = []

        for modelis in marke.modelis.all():
            naujas_modelis = {}
            naujas_modelis['modelis'] = modelis.automobilio_modelis
            naujas_modelis['metai'] = []
            for m in modelis.metai.all():
                naujas_modelis['metai'].append(str(m.automobilio_pagaminimo_metai))
            data['modeliai'].append(naujas_modelis)
        listas.append(data)
    print(listas)
    return render(request, 'registracija.html',context = {'listas':listas})
