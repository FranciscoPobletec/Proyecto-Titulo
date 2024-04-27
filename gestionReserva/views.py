from django.http import HttpResponse
import re
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Comerciante
from .forms import ComercianteForm
from gestionReserva.forms import ComercianteForm
from .models import Producto


def loginview(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        name = request.POST["username"]
        password = request.POST["password"]

        if not name or not password:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Por favor, completa todos los campos.'})

        user = authenticate(username=name, password=password)
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'Usuario y/o contraseña incorrectos.'})
        else:
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('index')


def registroview(request):
    if request.method == 'POST':
        form = ComercianteForm(request.POST)
        if form.is_valid():
            # Guardar el formulario si es válido
            user = form.save(commit=False)
            # Utilizar la contraseña ingresada en el formulario
            password = form.cleaned_data.get('contrasenia')
            # Asignar la contraseña al usuario
            user.set_password(password)
            # Guardar al usuario
            user.save()
            # Autenticar al usuario recién registrado
            username = form.cleaned_data.get('correo').split('@')[0]  
            user = authenticate(username=username, password=password)
            if user is not None:
                # Iniciar sesión para el usuario autenticado
                login(request, user)
                # Redirigir a la página de inicio después del registro exitoso
                return redirect('index')
            else:
                error = "No se pudo autenticar al usuario."
                return render(request, 'registro.html', {'form': form, 'error': error})
    else:
        # Si la solicitud no es POST, mostrar un formulario vacío para el registro
        form = ComercianteForm()
    return render(request, 'registro.html', {'form': form})


def indexview(request):
    return render(request, 'index.html')


def producto(request):
    productos = Producto.objects.all()  # Obtener todos los productos

    # Manejar la búsqueda si se envió un query en el formulario
    query = request.GET.get('q')
    if query:
        # Filtrar los productos por nombre
        productos = productos.filter(nombre__icontains=query)

    return render(request, 'Producto.html', {'productos': productos})


def salir(request):
    logout(request)
    return redirect("login")


def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    print("ID del producto a eliminar:", id)  # Imprime el ID del producto en la consola
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect('producto')
