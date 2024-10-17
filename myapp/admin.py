from django.contrib import admin
from .models import Parqueadero, Vehiculo, Cliente, Mapa, Usuario

admin.site.register(Parqueadero)
admin.site.register(Vehiculo)
admin.site.register(Cliente)
admin.site.register(Mapa)
admin.site.register(Usuario)