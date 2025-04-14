from django.db import models
from apps.cliente.models import Cliente
from apps.veiculo.models import Veiculo
from apps.core.enums import StatusOrdemServico

class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    descricao_problema = models.TextField()
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusOrdemServico.choices,
        default=StatusOrdemServico.ABERTA

    )

    def __str__(self):
        return f'OS #{self.pk} - {self.veiculo.placa} - {self.status}'
    