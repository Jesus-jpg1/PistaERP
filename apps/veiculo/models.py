from django.db import models
from apps.cliente.models import Cliente
from apps.core.validators import validar_placa
from apps.core.utils import gerar_placa


class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='veiculos')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=8, validators=[validar_placa], default=lambda: gerar_placa('mercosul'))
    ano = models.IntegerField()