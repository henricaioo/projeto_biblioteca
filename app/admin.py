from django.contrib import admin
from .models import *

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class EmprestimoInline(admin.TabularInline):
    model = Emprestimo
    extra = 1

class UfAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]

class AutorAdmin(admin.ModelAdmin):
    inlines = [LivroInline]

class EditoraAdmin(admin.ModelAdmin):
    inlines = [LivroInline]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "cpf", "data_nasc", "email", "telefone", "cidade"]

class LivroAdmin(admin.ModelAdmin):
    inlines = [EmprestimoInline]

class GeneroAdmin(admin.ModelAdmin):
    inlines = [LivroInline]

admin.site.register(Cidade)
admin.site.register(UF, UfAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo)
