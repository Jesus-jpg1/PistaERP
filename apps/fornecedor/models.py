from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    endereco = models.TextField()

def __str__(self):
    return f'{self.nome} - CNPJ: {self.cnpj}'
