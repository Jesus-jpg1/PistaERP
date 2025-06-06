from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VeiculoViewSet

router = DefaultRouter()
router.register(r'', VeiculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]