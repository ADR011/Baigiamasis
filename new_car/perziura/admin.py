from django.contrib import admin
# from .models import Order, Marke, Modelis, Metai

# from .models import City, Country, Person

from .models import Modelis, Marke, Order, Metai, Spalva



# Register your models here.
admin.site.register(Order)
admin.site.register(Marke)
admin.site.register(Modelis)
admin.site.register(Metai)
admin.site.register(Spalva)


# admin.site.register(Modelis)
# admin.site.register(Marke)
# admin.site.register(Klientas)
# admin.site.register(Order)
# admin.site.register(Metai)