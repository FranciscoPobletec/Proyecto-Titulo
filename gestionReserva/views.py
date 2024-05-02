from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Cliente, Local, Reserva
from .forms import ComercianteForm, LocalForm, ProductoForm
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

def loginview(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        name = request.POST.get("username")
        password = request.POST.get("password")
        if not name or not password:
            messages.error(request, 'Por favor, completa todos los campos.')
            return render(request, 'login.html', {'form': AuthenticationForm()})
        user = authenticate(username=name, password=password)
        if user is None:
            messages.error(request, 'Usuario y/o contraseña incorrectos.')
            return render(request, 'login.html', {'form': AuthenticationForm()})
        else:
            login(request, user)
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
    productos = Producto.objects.all().order_by(
        '-id')[:5]  # Obtener los últimos 5 productos

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


@require_POST
def eliminarProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente.")
    return redirect('producto')


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
                # Redireccionar a la página de éxito o donde sea necesario
                return redirect('index')
            else:
                messages.error(
                    request, "Ha ocurrido un error al guardar el producto")
        else:
            form = ProductoForm()
            # Filtrar solo los locales del usuario actual
            locales_usuario = Local.objects.filter(duenio=user)

            # Obtener todos los productos ordenados por la fecha de creación (o cualquier otro campo que desees)
            # Ordenados por ID en orden descendente
            productos = Producto.objects.order_by('-id')

            return render(request, 'registroProducto.html', {'form': form, 'locales': locales_usuario, 'productos': productos})
    except Local.DoesNotExist:
        messages.error(
            request, "Para agregar un producto, primero necesitas registrar un local")
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
        messages.error(
            request, "Para editar un producto, primero necesitas registrar un local.")
        # Redirigir a la página de inicio o a otra página según corresponda
        return redirect('index')

    # Obtener el producto a editar
    producto = get_object_or_404(Producto, id=producto_id)

    # Verificar si el producto pertenece al local del usuario actual
    if producto.local != local:
        # Si el producto no pertenece al local del usuario actual, mostrar un mensaje de error y redirigirlo a donde sea necesario
        messages.error(request, "No tienes permiso para editar este producto.")
        # Redirigir a la página de inicio o a otra página según corresponda
        return redirect('index')

    # Verificar si se envió un formulario de edición
    if request.method == 'POST':
        # Crear una instancia del formulario con los datos recibidos y la instancia del producto a editar
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            # Guardar los cambios en el producto
            form.save()
            # Mensaje de éxito
            messages.success(
                request, "Los cambios se guardaron correctamente.")
            # Redireccionar a alguna página de éxito o mostrar un mensaje de éxito
            return redirect('producto')
        else:
            # Agrega este print statement para depurar
            print("Formulario inválido:", form.errors)
    else:
        # Mostrar el formulario de edición con los datos del producto
        form = ProductoForm(instance=producto)

    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})


def calendario(request):
    today = datetime.today()
    reservas = Reserva.objects.all()  # Obtener todas las reservas
    context = {
        'fecha_actual': today,
        'reservas': reservas  # Pasar las reservas a la plantilla
    }
    return render(request, 'calendario.html', context)


def reserva(request, numero_orden):
    # Obtener la reserva con el número de orden especificado
    reserva = get_object_or_404(Reserva, numeroOrden=numero_orden)
    context = {
        'reserva': reserva
    }
    return render(request, 'reserva.html', context)


def historialReserva(request):
    # Obtener todos los clientes
    clientes = Cliente.objects.all()

    # Calcular el número de reservas para cada cliente
    for cliente in clientes:
        cliente.numero_reservas = Reserva.objects.filter(
            cliente=cliente).count()

    context = {
        'clientes': clientes
    }
    return render(request, 'historialReserva.html', context)


def historialCliente(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'historialCliente.html', context)


def calcular_puntaje_cliente(cliente):
    # Definir porcentajes asociados a cada estado
    porcentaje_estados = {
        '1': 10,  # Solicitado
        '2': 5,   # En Espera
        '3': 20,  # Retirado
        '4': -10,  # Cancelado Cliente
        '5': -15,  # Cancelado Comerciante
        '6': -5    # Expirado
    }

    # Inicializar el diccionario para contar la cantidad de reservas en cada estado
    contador_estados = {str(i): 0 for i in range(1, 7)}

    # Calcular el puntaje del cliente
    puntaje = 0
    reservas = cliente.reserva_set.all()
    for reserva in reservas:
        estado = reserva.estado
        if estado in porcentaje_estados:
            puntaje += porcentaje_estados[estado]
            # Incrementar el contador para el estado actual
            contador_estados[estado] += 1

    return puntaje, contador_estados


def rankingCliente(request):
    clientes = Cliente.objects.all()
    ranking = []
    for cliente in clientes:
        puntaje, contador_estados = calcular_puntaje_cliente(cliente)
        ranking.append((cliente, puntaje, contador_estados))

    # Ordenar el ranking por puntaje (de mayor a menor)
    ranking.sort(key=lambda x: x[1], reverse=True)

    context = {
        'ranking': ranking
    }
    return render(request, 'rankingCliente.html', context)
