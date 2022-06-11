from django.db import models
from django.contrib.auth.admin import User

# Create your models here


class Modelo(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    edicao = models.CharField(max_length=50, verbose_name="Edição")
    autor = models.CharField(max_length=50, verbose_name="Autor")
    materia = models.CharField(max_length=50, verbose_name= "Matéria")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=" Data de criação")
    data_atualizacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de atualização")

    class Meta:
        verbose_name_plural = "Modelos"

    def __str__(self):
        return "%s - %s - %s" % (self.nome, self.edicao, self.autor)


class Livro(models.Model):
    codigo = models.CharField(max_length=50, verbose_name="Código", unique=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, verbose_name="Modelo")
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Data de criação")
    data_atualizacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de atualização")

    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return "%s - %s" % (self.modelo, self.codigo)


class Emprestimo(models.Model):
    SITUACAO = [
        ('Devolvido', 'Devolvido'),
        ('Em empréstimo', 'Em empréstimo')
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="GRR")
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name="Livro")
    data_criacao = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Data de criaçãp")
    data_atualizacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de atualização")
    data_entrega = models.DateTimeField(verbose_name="Data de entrega")
    situacao = models.CharField(choices=SITUACAO, max_length=50, verbose_name="Situação")

    class Meta:
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return "%s - %s - %s" % (self.usuario, self.livro, self.situacao)


