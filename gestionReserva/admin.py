
from django.contrib import admin

from gestionReserva.models import Cliente, Comerciante, Local, Producto, Reserva


class LocalAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "direccion", "duenio"]
    search_fields = ["nombre", "direccion",
                     "duenio__nombre", "duenio__apellido"]
    list_filter = ["duenio"]
    list_per_page = 5


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "descripcion",
                    "cantidad", "precio", "local"]
    list_editable = ["nombre", "descripcion", "cantidad", "precio", "local"]
    search_fields = ["nombre", "descripcion", "local__nombre"]
    list_filter = ["local"]
    list_per_page = 5 
    
class LocalAdmin(admin.ModelAdmin):
    list_display = ["nombre", "direccion", "duenio"]
    search_fields = ["nombre", "direccion",
                        "duenio__nombre", "duenio__apellido"]
    list_filter = ["duenio"]
    list_per_page = 5


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "descripcion",
                    "cantidad", "precio", "local"]
    list_editable = ["nombre", "descripcion", "cantidad", "precio", "local"]
    search_fields = ["nombre", "descripcion", "local__nombre"]
    list_filter = ["local"]
    list_per_page = 5


class ReservaAdmin(admin.ModelAdmin):
    list_display = ["numeroOrden", "fechaInicio", "fechaTermino", "cliente", "cantidad_productos", "estado"]
    

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellidoP", "apellidoM",
                    "correo", "telefono", "direccion"]
    


admin.site.register(Comerciante)

admin.site.register(Local)

admin.site.register(Producto)

admin.site.register(Reserva)

admin.site.register(Cliente)