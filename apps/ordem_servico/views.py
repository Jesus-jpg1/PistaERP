from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import OrdemServico
from .serializers import OrdemServicoSerializer


class OrdemServicoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo OrdemServico.
    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete)
    para o modelo de Ordem de Serviço, utilizando o Django REST Framework.

    Atributos:
    - queryset: Define o conjunto de dados que será retornado pela view.
    - serializer_class: Define o serializer que será usado para converter os dados.
    - filter_backends: Define os filtros aplicados à view.
    - search_fields: Permite buscar fornecedores pelos campos 'nome' e 'email'.
    - permission_classes: Restringe o acesso a usuários autenticados.
    """
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['cliente__nome','veiculo__placa','status','descricao_problema']
    permission_classes = [IsAuthenticated]