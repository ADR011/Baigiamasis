from django.contrib import admin
from .models import Order, Marke, Modelis, Metai

# Register your models here.
admin.site.register(Order)
admin.site.register(Marke)
admin.site.register(Modelis)
admin.site.register(Metai)