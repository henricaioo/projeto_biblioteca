from django.contrib import admin
from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UfAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]

class AutorAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cidade"]

class EditoraAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "site", "cidade"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cpf", "data_nasc", "email", "telefone", "cidade"]

class GeneroAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]

class LivroAdmin(admin.ModelAdmin):
    list_display = ["id", "titulo", "genero", "autor", "editora", "preco", "publi"]

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ["id", "dataemprestimo", "livro", "user", "devolucao"]

admin.site.register(Cidade)
admin.site.register(UF, UfAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
