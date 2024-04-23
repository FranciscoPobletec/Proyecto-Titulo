from django.db import models
# Create your models here.




class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="Producto", null=True)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()

    def __str__(self):
        return self.numero


class Local(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=90)


def __str__(self):
    return self.nombre


class Reporte(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)


def __str__(self):
    return self.titulo
