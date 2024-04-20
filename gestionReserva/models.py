from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=30)



class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="Producto", null=True)


class Reserva(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()


class Local(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=90)


class Reporte(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)