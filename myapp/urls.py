from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view, name='index'),  
    path('parqueadero/<int:parqueadero_id>/', views.parqueadero_view, name='parqueadero'),
    path('usuario/<int:usuario_id>/', views.usuario_view, name='usuario'),  # Esta es tu URL
    path('vehiculo/<int:vehiculo_id>/', views.vehiculo_view, name='vehiculo'),
    path('mapa/<int:mapa_id>/', views.mapa_view, name='mapa'),
    ]
