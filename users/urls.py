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

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
