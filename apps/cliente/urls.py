from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet


# Cria um roteador padrão para registrar as rotas do ViewSet
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

# URLs do app Cliente
urlpatterns = [
    path('', include(router.urls)),
]