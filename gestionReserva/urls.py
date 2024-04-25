from . import views
from django.urls import include, path
from . views import indexview, loginview, registroview, salir
urlpatterns = [
    path('', loginview, name='login'),
    path('registro/', registroview, name='registro'), 
    path('index/', indexview, name='index'), 
    path('salir/', salir, name='salir'),
    path('producto/', views.producto, name='producto'),
    
    
]