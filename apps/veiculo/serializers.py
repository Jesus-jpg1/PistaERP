from rest_framework import serializers
from .models import Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Veiculo.
    Este serializer converte os dados do modelo Veiculo para JSON e vice-versa.
    Ele utiliza todos os campos do modelo Veiculo.
    """
    class Meta:
        model = Veiculo
        fields = '__all__'