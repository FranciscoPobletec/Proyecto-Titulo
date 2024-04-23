from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=50, null=True, blank= True)
    contrasenia = models.CharField(max_length=30, null=False)
    telefono = models.CharField(max_length=10, null=True, blank= True)
    direccion = models.CharField(max_length=90, null=False)

    class Meta:
        managed = True

class Familiar(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    familia = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        managed = True


class Comerciante(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=50, null=True, blank= True)
    contrasenia = models.CharField(max_length=30, null=False)
    telefono = models.CharField(max_length=10, null=True, blank= True)
    direccion = models.CharField(max_length=90, null=False)

class Local(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=90, null=False)
    duenio = models.ForeignKey(Comerciante, on_delete=models.CASCADE)


class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    cantidad = models.IntegerField(default =0)
    precio= models.IntegerField(default =0)
    imagen = models.ImageField(upload_to="Producto", null=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)





class Reserva(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()
    total =  models.IntegerField()


# class Reporte(models.Model):
#     titulo = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=200)


class Parametros(models.Model):
    parametro1 =models.CharField(max_length=50)
    parametro2 =models.CharField(max_length=50)
    parametro3 =models.CharField(max_length=50)