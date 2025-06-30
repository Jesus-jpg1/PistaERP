from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import OSPeca
from .serializers import OSPecaSerializer


class OSPecaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo OSPeca.
    Permite CRUD e busca pelos campos ordem_servico, peça e preço.
    """
    queryset = OSPeca.objects.all()
    serializer_class = OSPecaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['peca__nome', 'ordem_servico__id']
    permission_classes = [IsAuthenticated]