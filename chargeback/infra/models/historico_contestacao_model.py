from django.db import models

from chargeback.domain.value_objects.status_contestacao import STATUS_CONTESTACAO
from chargeback.infra.models.contestacao_model import ContestacaoModel


class HistoricoContestacaoModel(models.Model):
    contestacao = models.ForeignKey(
        ContestacaoModel,
        on_delete=models.CASCADE,
    )
    nome = models.SmallIntegerField(
        verbose_name="Nome do status",
        choices=STATUS_CONTESTACAO,
    )
    observacao = models.TextField(
        verbose_name="Observação",
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Contestação de {self.contestacao.cliente.nome} em {self.nome}"
    
    class Meta:
        verbose_name = "Histórico da Contestação"
        verbose_name_plural = "Histórico das Contestações"