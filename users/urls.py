from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('subasta/', views.subasta, name='subasta'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('crear-subasta/', views.crear_subasta, name='crear_subasta'),
    path('crear-carta/', views.crear_carta, name='crear_carta'),
    path('subasta/<int:subasta_id>/', views.subasta_detalle, name='subasta_detalle'),
    path('subasta/<int:subasta_id>/pujar/', views.realizar_puja, name='realizar_puja'),
    path('tienda/', views.tienda, name='tienda'),
    path('añadir-al-carrito/<int:carta_id>/', views.añadir_al_carrito, name='añadir_al_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('carritoDash/', views.carrito_dashboard, name='carrito_dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
