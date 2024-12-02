from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('opiniones/', views.lista_opiniones, name='lista_opiniones'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('crear_opinion/', views.crear_opinion, name='crear_opinion'),
]

