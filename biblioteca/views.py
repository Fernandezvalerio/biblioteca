from django.shortcuts import render

# crear tus vista aqui
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LibroForm, OpinionForm
from .models import Usuario, Libro, Opinion

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'biblioteca/crear_usuario.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/crear_libro.html', {'form': form})

def crear_opinion(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_opiniones')
    else:
        form = OpinionForm()
    return render(request, 'biblioteca/crear_opinion.html', {'form': form})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'biblioteca/lista_usuarios.html', {'usuarios': usuarios})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

def lista_opiniones(request):
    opiniones = Opinion.objects.all()
    return render(request, 'biblioteca/lista_opiniones.html', {'opiniones': opiniones})

