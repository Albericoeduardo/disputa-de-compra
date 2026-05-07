from django.db import models

from chargeback.domain.value_objects.status_contestacao import STATUS_CONTESTACAO
from chargeback.infra.models.contestacao_model import ContestacaoModel


class HistoricoContestacaoModel(models.Model):
    contestacao = models.ForeignKey(
        ContestacaoModel,
        on_delete=models.CASCADE,
    )
    status = models.SmallIntegerField(
        verbose_name="Status da contestacao",
        choices=STATUS_CONTESTACAO,
    )
    observacao = models.TextField(
        verbose_name="Observação",
        max_length=255,
        blank=True,
        null=True,
    )
    data_limite = models.DateTimeField(
        verbose_name="Data limite da etapa",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contestacao de {self.contestacao.cliente.nome} em {self.status}"
    
    class Meta:
        verbose_name = "Histórico da Contestação"
        verbose_name_plural = "Histórico das Contestações"