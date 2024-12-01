from django.contrib import admin

# registrar modelos aqui
from django.contrib import admin
from .models import Usuario, Libro, Opinion

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Opinion)

