from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Subasta

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def index(request):
    return render(request, 'users/index.html')

def subasta(request):
    subastas = Subasta.objects.all()
    for subasta in subastas:
        subasta.end_time = subasta.end_time()  # Añadir el cálculo del tiempo de finalización

    return render(request, 'users/subastas.html', {'subastas': subastas})
