from . import views
from django.urls import include, path
from .views import registroProducto, eliminarProducto, indexview, loginview, registroview, salir,editarProducto

urlpatterns = [
    path('', loginview, name='login'),  # Cambia 'login' a 'Login' aquí
    path('registro/', registroview, name='registro'), 
    path('index/', indexview, name='index'), 
    path('salir/', salir, name='salir'),
    path('producto/', views.producto, name='producto'),
    path('eliminarProducto/<pk>/', eliminarProducto.as_view(), name='eliminar_producto'),
    path('local/', views.local, name='local'),
    path('registroProducto/', registroProducto, name='registroProducto'),
    path('editarProducto/<int:producto_id>/', editarProducto, name='editarProducto')
]
