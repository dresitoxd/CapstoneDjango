from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .models import *
from .forms import SubastaForm, PujaForm, CartaForm
from django.utils import timezone

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
    subastas_activas = []
    for subasta in subastas:
        # Llamamos al método end_time para obtener el datetime de finalización
        subasta_end_time = subasta.end_time()

        # Comparamos con la hora actual
        if subasta_end_time > timezone.now():
            subastas_activas.append(subasta)

    return render(request, 'users/subastas.html', {'subastas': subastas_activas})

def crear_subasta(request):
    if request.method == 'POST':
        form = SubastaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subasta')  # Cambia 'subasta' según la URL que quieras redirigir después de crear la subasta
    else:
        form = SubastaForm()

    return render(request, 'users/crear_subasta.html', {'form': form})

def crear_carta(request):
    if request.method == 'POST':
        form = CartaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda')  # Cambia 'subasta' según la URL que quieras redirigir después de crear la subasta
    else:
        form = CartaForm()

    return render(request, 'users/crear_carta.html', {'form': form})

@login_required

def realizar_puja(request, subasta_id):
    subasta = get_object_or_404(Subasta, id=subasta_id)

    if subasta.end_time() <= timezone.now():
        # La subasta ha terminado
        return redirect('subasta_terminada', subasta_id=subasta.id)
    
    if request.method == 'POST':
        form = PujaForm(request.POST)
        if form.is_valid():
            puja = form.save(commit=False)
            puja.subasta = subasta
            puja.user = request.user
            if subasta.pujas.exists():
                max_puja = subasta.pujas.order_by('-amount').first()
                if puja.amount <= max_puja.amount:
                    form.add_error('amount', 'La puja debe ser mayor que la última puja.')
                    return render(request, 'users/realizar_puja.html', {'form': form, 'subasta': subasta})
            puja.save()
            return redirect('users:subastas')  # Redirige a la página de subastas
    else:
        form = PujaForm()

    return render(request, 'subasta/realizar_puja.html', {'form': form, 'subasta': subasta})

def subasta_detalle(request, subasta_id):
    subasta = get_object_or_404(Subasta, id=subasta_id)
    pujas = subasta.pujas.all()
    return render(request, 'users/subastas.html', {'subasta': subasta, 'pujas': pujas})


def tienda(request):
    cartas = Carta.objects.all()  # Asegúrate de que estás pasando todas las cartas
    return render(request, 'users/tienda.html', {'cartas': cartas})

@login_required
def añadir_al_carrito(request, carta_id):
    carta = Carta.objects.get(id=carta_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user)

    # Verificar si la carta ya está en el carrito
    item_carrito, created = ItemCarrito.objects.get_or_create(carrito=carrito, carta=carta)

    if not created:
        # Si ya existe, incrementar la cantidad
        item_carrito.cantidad += 1
        item_carrito.save()

    return redirect('carrito')  # Redirigir a la página del carrito

@login_required
def carrito(request):
    carrito = Carrito.objects.get(user=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)

    return render(request, 'users/carrito_dashboard.html', {'carrito': carrito, 'items': items})

def carrito_dashboard(request):
    try:
        # Obtener el carrito del usuario
        carrito = Carrito.objects.get(user=request.user)
        items = ItemCarrito.objects.filter(carrito=carrito)

        # Calcular el total del carrito
        total_carrito = sum(item.total for item in items)

    except Carrito.DoesNotExist:
        carrito = None
        items = []
        total_carrito = 0

    return render(request, 'users/carrito_dashboard.html', {
        'carrito': carrito,
        'items': items,
        'total_carrito': total_carrito
    })
