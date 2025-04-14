from django.contrib import admin
from .models import OrdemServico

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cliente',
        'veiculo',
        'status',
        'data_entrada',
        'data_saida'
    )
    search_fields = ('cliente__nome', 'veiculo__placa')
    list_filter = ('status', 'data_entrada', 'data_saida')
    date_hierarchy = 'data_entrada'
