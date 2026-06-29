from django.contrib import admin

from .models import Mensagem, Categoria


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "criada_em", )
    list_filter = ("categoria", )
    search_fields = ("titulo", "conteudo", )



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome", )
    search_fields = ("nome", )


