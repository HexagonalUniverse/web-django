
from django.urls import path, URLPattern

from . import views


urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),

    # trem novo
    path("sobre/", views.sobre, name="sobre"),

    # outro trem novo
    path("nova/", views.nova_mensagem, name="nova_mensagem"),

    # editar
    path("mensagens/<int:id>/editar/", views.editar_mensagem, name="editar_mensagem"),

    # remover
    path("mensagens/<int:id>/remover/", views.remover_mensagem, name="remover_mensagem"),  # ← novo
]
