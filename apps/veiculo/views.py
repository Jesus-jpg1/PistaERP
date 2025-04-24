from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Veiculo
from .serializers import VeiculoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Veiculo.
    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete)
    para o modelo Veiculo, utilizando o Django REST Framework.

    Atributos:
    - queryset: Define o conjunto de dados que será retornado pela view.
    - serializer_class: Define o serializer que será usado para converter os dados.
    - filter_backends: Define os filtros aplicados à view.
    - search_fields: Permite buscar veículos pelos campos 'placa', 'marca' e 'modelo'.
    - permission_classes: Restringe o acesso a usuários autenticados.
    """
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['placa','marca','modelo']
    permission_classes = [IsAuthenticated]
