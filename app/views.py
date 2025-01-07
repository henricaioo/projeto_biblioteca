from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        ufs = UF.objects.all()
        return render(request, 'index.html', {'ufs': ufs})
    def post(self, request):
        pass

class AutorView(View):
    def get(self, request, *args, **kwargs):
        autordata = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autordata})
    
class EditoraView(View):
    def get(self, request, *args, **kwargs):
        editoradata = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoradata})

class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        emprestimodata = Emprestimo.objects.all()
        return render(request, 'emprestimo.html', {'emprestimos': emprestimodata})

class GeneroView(View):
    def get(self, request, *args, **kwargs):
        generodata = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generodata})
    
class LivroView(View):
    def get(self, request, *args, **kwargs):
        livrodata = Livro.objects.all()
        return render(request, 'livro.html', {'livros': livrodata})
    
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidadedata = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidadedata})

class UfView(View):
    def get(self, request, *args, **kwargs):
        ufdata = UF.objects.all()
        return render(request, 'ufs.html', {'ufs': ufdata})
    
class UserView(View):
    def get(self, request, *args, **kwargs):
        userdata = User.objects.all()
        return render(request, 'user.html', {'users': userdata})