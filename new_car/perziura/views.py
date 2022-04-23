from multiprocessing import context
from django.shortcuts import render
from .models import Order

def perziura(request):
    orders = Order.objects.all()
    context={'orders': orders}
    print(orders)
    return render(request, 'perziura.html', context=context)

def pradinis(request):
#    return HttpResponse("Hello, world. You're at the registracija page.")
    return render(request, 'pradinis.html')
