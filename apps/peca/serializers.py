from rest_framework import serializers
from .models import Peca


class PecaSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Peça.
    Este serializer converte os dados da Peça para JSON e vice-versa.
    Ele utiliza todos os campos do modelo Peça.
    """
    class Meta:
        model = Peca
        fields = '__all__'