from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, blank=True, null=True)
    endereco = models.TextField()

    def __str__(self):
        return f"{self.nome} ({self.cpf})"