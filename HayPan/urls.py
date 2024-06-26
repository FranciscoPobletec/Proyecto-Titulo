"""
URL configuration for HayPan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from gestionReserva import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestionReserva.urls')),
    path('producto/', views.producto, name='producto'),
    path('eliminarProducto/<int:producto_id>/', views.eliminarProducto, name='eliminar_producto'),
    path('local/', views.local, name='local'),
    path('registroProducto/', views.registroProducto, name='registroProducto'),
    path('editarProducto/<int:producto_id>/',views.editarProducto, name='editarProducto'),
    path('calendario/', views.calendario, name='calendario'),
    path('reserva/<int:numero_orden>/', views.reserva, name='reserva'),
    path('historialReserva/', views.historialReserva, name='historialReserva'),
    path('rankingCliente/', views.rankingCliente, name='rankingCliente'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)