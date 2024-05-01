from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidoP = models.CharField(max_length=50, null=False)
    apellidoM = models.CharField(max_length=50, null=False)
    correo = models.EmailField(
        max_length=50, null=True, blank=True, unique=True)
    contrasenia = models.CharField(max_length=30, null=False)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.CharField(max_length=90, null=False)

    class Meta:
        managed = True


class Familiar(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellidoP = models.CharField(max_length=50, null=False)
    apellidoM = models.CharField(max_length=50, null=False)
    familia = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        managed = True


class Comerciante(AbstractUser):
    nombre = models.CharField(max_length=50, null=False)
    apellidoP = models.CharField(max_length=50, null=False)
    apellidoM = models.CharField(max_length=50, null=False)
    contrasenia = models.CharField(max_length=30, null=False)
    correo = models.EmailField(
        max_length=50, null=True, blank=True, unique=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.CharField(max_length=90, null=False)


class Local(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=90, null=False)
    duenio = models.ForeignKey(
        Comerciante, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="Producto", null=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    numeroOrden = models.IntegerField()
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    productos = models.ManyToManyField(Producto)
    tipo_choices = [
        ('1', 'Solicitado'),
        ('2', 'En Espera'),
        ('3', 'Retirado'),
        ('4', 'Cancelado Cliente'),
        ('5', 'Cancelado Comerciante'),
        ('6', ' Expirado Expirado'),
    ]
    estado = models.CharField(
        max_length=10, choices=tipo_choices, default='Solicitado')
    """
        1 Solicitado
        2 En Espera
        3 Retirado
        4 Cancelado Cliente
        5 Cancelado Comerciante
        6 Expirado

    """

    # Solicitado- En espera, Retirado - Cancelado Cliente Cancelado Comercian


# class Reporte(models.Model):
#     titulo = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=200)


class Parametros(models.Model):
    parametro1 = models.CharField(max_length=50)
    parametro2 = models.CharField(max_length=50)
    parametro3 = models.CharField(max_length=50)
