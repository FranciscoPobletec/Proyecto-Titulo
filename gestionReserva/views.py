from django.http import HttpResponse
import re
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Local
from .forms import ComercianteForm, LocalForm,ProductoForm
from .models import Producto
from django.views.generic import  DeleteView
from django.contrib.auth.decorators import login_required


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
                return redirect('Login')
            else:
                error = "No se pudo autenticar al usuario."
                return render(request, 'registro.html', {'form': form, 'error': error})
    else:
        # Si la solicitud no es POST, mostrar un formulario vacío para el registro
        form = ComercianteForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def indexview(request):
    user = request.user  # Obtiene el usuario actual

    # Obtener todos los productos
    productos = Producto.objects.all().order_by('-id')[:5]  # Obtener los últimos 5 productos

    # Verifica si el usuario tiene un local registrado
    try:
        local = Local.objects.get(duenio=user)
        print("Usuario tiene un local registrado:", local)
        return render(request, 'index.html', {'local': local, 'productos': productos})
    except Local.DoesNotExist:
        print("Usuario no tiene un local registrado.")
        return render(request, 'index.html', {'alerta': True, 'productos': productos})


def producto(request):
    # Obtener todos los productos
    productos = Producto.objects.all()
    print("Productos obtenidos inicialmente:", productos)

    # Manejar la búsqueda si se envió un query en el formulario
    query = request.GET.get('q')
    if query:
        # Filtrar los productos por descripción
        productos = productos.filter(descripcion__icontains=query)
        # Imprimir en la consola para verificar si se obtienen los productos correctamente después de la búsqueda
        print("Productos obtenidos después de la búsqueda por descripción:", productos)

    return render(request, 'producto.html', {'productos': productos})


class eliminarProducto(DeleteView):
    MODEL = Producto
    success_url = reverse_lazy('producto:producto')


def salir(request):
    logout(request)
    return redirect("login")


def local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            local = form.save(commit=False)
            # Asignar el dueño del local al comerciante actualmente autenticado
            local.duenio = request.user
            local.save()
            # Redireccionar a una página de éxito
            return redirect('index')
    else:
        form = LocalForm()
    return render(request, 'local.html', {'form': form})

from .models import Producto

@login_required
def registroProducto(request):
    user = request.user
    try:
        local = Local.objects.get(duenio=user)
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.local = local  # Asociar el producto al local del usuario
                producto.save()
                messages.success(request, "Producto guardado correctamente")
                return redirect('index')  # Redireccionar a la página de éxito o donde sea necesario
            else:
                messages.error(request, "Ha ocurrido un error al guardar el producto")
        else:
            form = ProductoForm()
            # Filtrar solo los locales del usuario actual
            locales_usuario = Local.objects.filter(duenio=user)

            # Obtener todos los productos ordenados por la fecha de creación (o cualquier otro campo que desees)
            productos = Producto.objects.order_by('-id')  # Ordenados por ID en orden descendente

            return render(request, 'registroProducto.html', {'form': form, 'locales': locales_usuario, 'productos': productos})
    except Local.DoesNotExist:
        messages.error(request, "Para agregar un producto, primero necesitas registrar un local")
        return redirect('local')

    # Si la solicitud no es POST y no se cumplen las condiciones anteriores, retornar un HttpResponse vacío
    return HttpResponse()





@login_required
def editarProducto(request, producto_id):
    # Obtener el usuario actual
    usuario = request.user

    # Obtener el local asociado al usuario actual
    try:
        local = Local.objects.get(duenio=usuario)
    except Local.DoesNotExist:
        # Si el usuario no tiene un local registrado, mostrar un mensaje de error y redirigirlo a donde sea necesario
        messages.error(request, "Para editar un producto, primero necesitas registrar un local.")
        return redirect('index')  # Redirigir a la página de inicio o a otra página según corresponda

    # Obtener el producto a editar
    producto = get_object_or_404(Producto, id=producto_id)

    # Verificar si el producto pertenece al local del usuario actual
    if producto.local != local:
        # Si el producto no pertenece al local del usuario actual, mostrar un mensaje de error y redirigirlo a donde sea necesario
        messages.error(request, "No tienes permiso para editar este producto.")
        return redirect('index')  # Redirigir a la página de inicio o a otra página según corresponda

    # Verificar si se envió un formulario de edición
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos recibidos y la instancia del producto a editar
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            # Guardar los cambios en el producto
            form.save()
            # Mensaje de éxito
            messages.success(request, "Los cambios se guardaron correctamente.")
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('producto')
        else:
            print("Formulario inválido:", form.errors)  # Agrega este print statement para depurar
    else:
        # Mostrar el formulario de edición con los datos del producto
        form = ProductoForm(instance=producto)

    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})