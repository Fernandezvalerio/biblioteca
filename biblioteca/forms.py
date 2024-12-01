from django import forms
from .models import Usuario, Libro, Opinion

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero']

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['usuario', 'libro', 'texto']
