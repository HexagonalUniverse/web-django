from django.shortcuts import render

from .models import Mensagem


def index(request):
    mensagens: list[Mensagem] = Mensagem.objects.all()
    return render(
        request,
        "home/index.html",
        {
            "mensagens": mensagens,
        },
    )

