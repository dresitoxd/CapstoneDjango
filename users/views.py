from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import Subasta
from .forms import SubastaForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada {username}. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

def index(request):
    return render(request, 'users/index.html')

def subasta(request):
    subastas = Subasta.objects.all()
    for subasta in subastas:
        subasta.end_time = subasta.end_time()  # Añadir el cálculo del tiempo de finalización

    return render(request, 'users/subastas.html', {'subastas': subastas})

def crear_subasta(request):
    if request.method == 'POST':
        form = SubastaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subasta')  # Cambia 'subasta' según la URL que quieras redirigir después de crear la subasta
    else:
        form = SubastaForm()

    return render(request, 'users/crear_subasta.html', {'form': form})
