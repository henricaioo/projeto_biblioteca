from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length = 2)

    class Meta:
        verbose_name_plural = 'Unidades Federais'

    def __str__(self):
        return self.sigla
    
class Cidade(models.Model):
    cidade = models.CharField(max_length = 80)
    uf = models.ForeignKey(UF, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.cidade
    
class Autor(models.Model):
    nome = models.CharField(max_length = 80)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    nome = models.CharField(max_length = 80)
    site = models.CharField(max_length = 80)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Editoras'

    def __str__(self):
        return self.nome
    
class User(models.Model):
    nome = models.CharField(max_length = 80)
    cpf = models.CharField(max_length = 11)
    data_nasc = models.DateField()
    email = models.CharField(max_length = 50)
    telefone = models.CharField(max_length = 20)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome
    
class Genero(models.Model):
    nome = models.CharField(max_length = 80)

    class Meta:
        verbose_name_plural = 'Gêneros'

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length = 80)
    genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete = models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    publi = models.DateField()

    class Meta:
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo
    
class Emprestimo(models.Model):
    dataemprestimo= models.DateField()
    livro = models.ForeignKey(Livro, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    devolucao = models.DateField()