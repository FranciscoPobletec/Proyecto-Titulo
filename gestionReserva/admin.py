from django.contrib import admin
from .models import Usuario, Producto, Reserva, Local, Reporte

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'contraseña')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'cantidad', 'precio')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'estado')

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion')


