from django.contrib import admin
from .models import Modelo, Livro, Emprestimo

# Register your models here.

admin.site.register(Modelo)
admin.site.register(Livro)
admin.site.register(Emprestimo)
