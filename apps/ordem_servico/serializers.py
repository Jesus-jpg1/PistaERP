from rest_framework import serializers
from .models import OrdemServico


class OrdemServicoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Ordem de Serviço.
    Este serializer converte os dados do modelo OrdemServico para JSON e vice-versa.
    Ele utiliza todos os campos do modelo   .
    """
    class Meta:
        model = OrdemServico
        fields = '__all__'