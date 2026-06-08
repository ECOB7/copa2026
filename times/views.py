from django.http import JsonResponse
from .models import Selecao, Jogador


def listar_selecoes(request):
    selecoes = Selecao.objects.all()

    data = list(
        selecoes.values(
            "id",
            "nome",
            "continente",
            "tecnico"
        )
    )

    return JsonResponse(data, safe=False)


def listar_jogadores(request):
    jogadores = Jogador.objects.all()

    data = list(
        jogadores.values(
            "id",
            "nome",
            "idade",
            "posicao",
            "numero",
            "selecao_id"
        )
    )

    return JsonResponse(data, safe=False)


def listar_jogadores_brasil(request):
    jogadores = Jogador.objects.filter(selecao__nome="Brasil")

    data = list(
        jogadores.values(
            "id",
            "nome",
            "posicao",
            "numero"
        )
    )

    return JsonResponse(data, safe=False)