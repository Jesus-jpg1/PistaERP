from rest_framework import serializers
from .models import Fornecedor


class FornecedorSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Fornecedor.
    Este serializer converte os dados do modelo Fornecedor para JSON e vice-versa.
    Ele utiliza todos os campos do modelo Fornecedor.
    """
    class Meta:
        model = Fornecedor
        fields = '__all__'