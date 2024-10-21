from django.urls import path
from .views import index_view, parqueadero_view, usuario_view, vehiculo_view, mapa_view

urlpatterns = [
    path('', index_view, name='index'),  
    path('parqueadero/<int:parqueadero_id>/', parqueadero_view, name='parqueadero'),
    path('usuario/<int:usuario_id>/', usuario_view, name='usuario'),
    path('vehiculo/<int:vehiculo_id>/', vehiculo_view, name='vehiculo'),
    path('mapa/<int:mapa_id>/', mapa_view, name='mapa'),
]
