from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Klientas, Modelis


from multiprocessing import context
from django.shortcuts import render
from .models import Order, Marke, Metai
from django.http import HttpResponse



def perziura(request):
    klientai = Klientas.objects.all()
    context={'klientai': klientai}
    print(klientai)
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
        new = Order(vardas = user_name, pavarde = user_last_name, email = user_email)
        new.save()
        marke = Marke(marke = marke)
        modelis = Modelis(modelis = modelis)
        metai = Metai(metai = metai)
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
        print(marke.modelis.all())
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
    print(listas)
    return render(request, 'registracija.html')#,context = {'listas':listas})


################################################################

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Klientas, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_modeliai(request):
    marke_id = request.GET.get('marke_id')
    modeliai = Modelis.objects.filter(marke_id=marke_id).all()
    return render(request, 'modelis_dropdown_list_options.html', {'modeliai': modeliai})
    #return JsonResponse(list(modeliai.values('id', 'name')), safe=False)


