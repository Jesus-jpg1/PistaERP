from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated


class ClienteViewSet (viewsets.ModelViewSet):
    """
    ViewSet para o modelo Cliente.
    Este ViewSet fornece as operações padrão de CRUD (Create, Read, Update, Delete)
    para o modelo Cliente, utilizando o Django REST Framework.

    Atributos:
    - queryset: Define o conjunto de dados que será retornado pela view.
    - serializer_class: Define o serializer que será usado para converter os dados.
    - filter_backends: Define os filtros aplicados à view.
    - search_fields: Permite buscar clientes pelos campos 'nome' e 'email'.
    - permission_classes: Restringe o acesso a usuários autenticados.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'email']
    permission_classes = [IsAuthenticated]