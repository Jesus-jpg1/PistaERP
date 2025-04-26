from django.db import models
from apps.core.validators import validar_cnpj

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, validators=[validar_cnpj])
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return f'{self.nome} - CNPJ: {self.cnpj}'
