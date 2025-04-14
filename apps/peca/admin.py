from django.contrib import admin

from .models import Peca

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade_estoque', 'fornecedor')
    search_fields = ('nome',)
    list_filter = ('fornecedor',)
