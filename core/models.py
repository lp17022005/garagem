from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def _str_(self):
        return self.nome

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Cores(models.Model):
    cor = models.CharField(max_length=50)

    def _str_(self):
        return self.cor

class Motores(models.Model):
    motor = models.CharField(max_length=100)

    def _str_(self):
        return self.motor

class Valor(models.Model):
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.preco} ({self.quantidade})'

class Carro(models.Model):
    ano = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return self.ano