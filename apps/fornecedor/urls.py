from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FornecedorViewSet

# Cria um roteador padrão para registrar as rotas do ViewSet
router = DefaultRouter()
router.register(r'', FornecedorViewSet)  # Registra o ViewSet sem prefixo, acessível diretamente na raiz

# Define as URLs do app Fornecedor
urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas geradas pelo roteador
]