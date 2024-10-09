from django.shortcuts import render, redirect
from .models import Parqueadero, Vehiculo, Cliente

def inicio(request):
    return render(request, 'inicio.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        # Lógica para agregar un vehículo
        pass
    return render(request, 'agregar_vehiculo.html')

def detalle_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def generar_factura(request):
    if request.method == 'POST':
        # Lógica para generar una factura
        pass
    return render(request, 'generar_factura.html')