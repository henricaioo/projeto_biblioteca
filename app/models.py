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

class Pessoa(models.Model):
    nome = models.CharField(max_length = 255, default = '')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    email = models.CharField(max_length = 50, default = '')
    telefone = models.CharField(max_length = 20, default = '')

    class Meta:
        abstract = True

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length = 11, default = '')
    data_nasc = models.DateField(default = "1600-12-01")

    class Meta:
        abstract = True

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length = 14, default = '')
    data_fund = models.DateField(default = "1600-12-01")

    class Meta:
        abstract = True

class User(PessoaFisica):
    pass

class Autor(PessoaFisica):
    pass

class Editora(PessoaJuridica):
    site = models.CharField(max_length = 50, default = '')
    
class Genero(models.Model):
    nome = models.CharField(max_length = 80, default = '')

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
    devolucao = models.DateField(default = "1600-12-01")