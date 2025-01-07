from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import include, path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path('autores/', AutorView.as_view(), name='autores'),
    path('cidades/', CidadeView.as_view(), name='cidades'),
    path('editoras/', EditoraView.as_view(), name='editoras'),
    path('emprestimos/', EmprestimoView.as_view(), name='emprestimos'),
    path('generos/', GeneroView.as_view(), name='generos'),
    path('livros/', LivroView.as_view(), name='livros'),
    path('ufs/', UfView.as_view(), name='ufs'),
    path('users/', UserView.as_view(), name='users'),
]
