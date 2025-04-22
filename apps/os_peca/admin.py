from django.contrib import admin
from .models import OSPeca

@admin.register(OSPeca)
class OSPecaAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'peca', 'quantidade', 'preco_unitario')
    search_fields = ('peca__nome', 'ordem_servico__id')
    list_filter = ('peca',)
