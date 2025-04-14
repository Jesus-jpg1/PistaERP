from django.db import models

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    fornecedor = models.ForeignKey('fornecedor.Fornecedor', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.descricao[:30]}'
