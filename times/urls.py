from django.urls import path
from .views import (
    listar_selecoes,
    listar_jogadores,
    listar_jogadores_brasil
)

urlpatterns = [
    path('api/selecoes/', listar_selecoes),
    path('api/jogadores/', listar_jogadores),
    path('api/jogadores/brasil/', listar_jogadores_brasil),
]