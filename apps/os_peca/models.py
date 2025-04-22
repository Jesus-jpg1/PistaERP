from django.db import models
from apps.ordem_servico.models import OrdemServico
from apps.peca.models import Peca

class OSPeca(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade}x {self.peca.nome} (OS #{self.ordem_servico.pk})'
