# from django.shortcuts import render, redirect
# from .forms import LoginForm, RegistroForm
# from django.contrib.auth import authenticate, login


# # Create your views here.
# def loginview(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data['contraseña_preview'] = form.cleaned_data['contraseña']
#     return render(request, 'registration/login.html', {'form': form})

# def registroview(request):
#     if request.method == 'POST':
#         form = RegistroForm(request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect('/login.html')
#     else:
#         form = RegistroForm()
#     return render(request, '/registro.html', {'form': form})


# def indexiew(request):
#     return render(request, 'cliente/index.html',)