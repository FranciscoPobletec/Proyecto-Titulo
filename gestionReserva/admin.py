from django.contrib import admin
from .models import  Producto, Reserva, Local, Reporte


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'cantidad', 'precio')
    fields = ('nombre', 'descripcion', 'cantidad', 'precio')  # Agregar los campos que deseas editar
    search_fields = ["nombre"]
    list_per_page = 10

    
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'estado')
    fields = ('numero', 'fecha', 'estado')  # Agregar los campos que deseas editar

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    fields = ('nombre', 'direccion')  # Agregar los campos que deseas editar

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')
    fields = ('titulo', 'descripcion')  # Agregar los campos que deseas editar



