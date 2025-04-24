from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Peca
from .serializers import PecaSerializer

class PecaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Peça.
    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete)
    para o modelo Peça, utilizando o Django REST Framework.

    Atributos:
    - queryset: Define o conjunto de dados que será retornado pela view.
    - serializer_class: Define o serializer que será usado para converter os dados.
    - filter_backends: Define os filtros aplicados à view.
    - search_fields: Permite buscar Peças pelos campos 'nome', 'fornecedor' e 'descrição'.
    - permission_classes: Restringe o acesso a usuários autenticados.
    """
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome','descricao','fornecedor__nome']
    permission_classes = [IsAuthenticated]