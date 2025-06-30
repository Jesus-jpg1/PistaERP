from rest_framework import serializers
from .models import OSPeca


class OSPecaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo OSPeca, relacionamento de Ordem de Serviço e Peça.
    Converte os dados entre JSON e o modelo, incluindo ordem de serviço, peça, quantidade e preço unitário.
    """
    class Meta:
        model = OSPeca
        fields = '__all__'