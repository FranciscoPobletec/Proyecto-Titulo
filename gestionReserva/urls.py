from . import views
from django.urls import include, path
from .views import registroProducto, eliminarProducto, indexview, loginview, registroview, salir,editarProducto

urlpatterns = [
    path('', loginview, name='login'),  # Cambia 'login' a 'Login' aquí
    path('login/', loginview, name='Login'),
    path('registro/', registroview, name='registro'), 
    path('index/', indexview, name='index'), 
    path('salir/', salir, name='salir'),
    path('producto/', views.producto, name='producto'),
    path('eliminarProducto/<int:producto_id>/', eliminarProducto, name='eliminar_producto'),
    path('local/', views.local, name='local'),
    path('registroProducto/', registroProducto, name='registroProducto'),
    path('editarProducto/<int:producto_id>/', editarProducto, name='editarProducto'),
    path('calendario/', views.calendario, name='calendario'),
    path('reserva/<int:numero_orden>/', views.reserva, name='reserva'),
    path('historialReserva/', views.historialReserva, name='historialReserva'),
    path('historialCliente/', views.historialCliente, name='historialCliente'),
    path('rankingCliente/', views.rankingCliente, name='rankingCliente'),
    ]