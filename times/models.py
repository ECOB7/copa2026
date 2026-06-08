from django.db import models

class Selecao(models.Model):
    nome = models.CharField(max_length=100)
    continente = models.CharField(max_length=50)
    tecnico = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    posicao = models.CharField(max_length=50)
    numero = models.IntegerField()

    selecao = models.ForeignKey(
        Selecao,
        on_delete=models.CASCADE,
        related_name='jogadores'
    )

    def __str__(self):
        return self.nome