from django.db import models

from chargeback.chargeback.domain.constantes import STATUS_CONTESTACAO
from chargeback.chargeback.infra.persistence.models.contestacao import Contestacao


class HistoricoContestacoes(models.Model):
    contestacao = models.ForeignKey(
        Contestacao,
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
        verbose_name = "Histórico de Contestação"
        verbose_name_plural = "Históricos de Contestação"