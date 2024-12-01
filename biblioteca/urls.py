from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('opiniones/crear/', views.crear_opinion, name='crear_opinion'),
    path('opiniones/', views.lista_opiniones, name='lista_opiniones'),
]
