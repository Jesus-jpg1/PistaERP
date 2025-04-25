from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import Fornecedor
from .serializers import FornecedorSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Fornecedor.
    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete)
    para o modelo Fornecedor, utilizando o Django REST Framework.

    Atributos:
    - queryset: Define o conjunto de dados que será retornado pela view.
    - serializer_class: Define o serializer que será usado para converter os dados.
    - filter_backends: Define os filtros aplicados à view.
    - search_fields: Permite buscar fornecedores pelos campos 'nome' e 'email'.
    - permission_classes: Restringe o acesso a usuários autenticados.
    """
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'email']
    permission_classes = [IsAuthenticated]