from django.shortcuts import render, get_object_or_404
from .models import Parqueadero, Usuario, Vehiculo, Mapa

def index_view(request):
    return render(request, 'index.html')

def parqueadero_view(request, parqueadero_id):
    parqueadero = get_object_or_404(Parqueadero, id=parqueadero_id)
    return render(request, 'parqueadero.html', {'parqueadero': parqueadero})

def usuario_view(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    return render(request, 'usuario.html', {'usuario': usuario})

def vehiculo_view(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    return render(request, 'vehiculo.html', {'vehiculo': vehiculo})

def mapa_view(request, mapa_id):
    mapa = get_object_or_404(Mapa, id=mapa_id)
    return render(request, 'mapa.html', {'mapa': mapa})


