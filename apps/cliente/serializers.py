from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Cliente.
    Este serializer converte os dados do modelo Cliente para JSON e vice-versa.
    Ele utiliza todos os campos do modelo Cliente.
    """
    class Meta:
        model = Cliente
        fields = '__all__'