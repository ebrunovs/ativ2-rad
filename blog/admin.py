from django.contrib import admin
from .models import Autor, Editora, Livro, Publica

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
	list_display = ('id', 'nome')
	search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
	list_display = ('id', 'ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora')
	search_fields = ('ISBN', 'titulo')

@admin.register(Publica)
class PublicaAdmin(admin.ModelAdmin):
	list_display = ('id', 'livro', 'autor')
	search_fields = ('livro__titulo', 'autor__nome')
