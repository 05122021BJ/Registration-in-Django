from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=254)
    cpf = models.CharField('CPF', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantiddade em Estoque')

    def __str__(self):
        return self.nome
