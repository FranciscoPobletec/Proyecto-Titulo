import re
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
    if request.method == 'GET':
        return render(request, 'registro.html', {'form': UserCreationForm()})
    else:
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            return render(request, "registro.html", {'form': UserCreationForm(), 'error': "Las contraseñas no coinciden"})
        elif not (8 <= len(password1) <= 20):
            return render(request, "registro.html", {'form': UserCreationForm(), 'error': "La contraseña debe tener entre 8 y 20 caracteres"})
        else:
            name = request.POST["username"]
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', name):
                return render(request, "registro.html", {'form': UserCreationForm(), 'error': "El nombre de usuario debe ser una dirección de correo válida"})
            elif User.objects.filter(username=name).exists():
                return render(request, "registro.html", {'form': UserCreationForm(), 'error': "El nombre de usuario ya está en uso"})
            else:
                user = User.objects.create_user(
                    username=name, password=password1)
                user.save()
                # Iniciar sesión automáticamente después del registro
                login(request, user)
                messages.success(request, "¡Usuario registrado exitosamente!")
                # Redireccionar a las obras destacadas
                return redirect('login')


def indexview(request):
    return render(request, 'index.html')


def salir(request):
    logout(request)
    return redirect("login")
