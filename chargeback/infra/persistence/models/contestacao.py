from django.db import models

from chargeback.chargeback.domain.constantes import (
    STATUS_CONTESTACAO,
    TIPO_CONTESTACAO,
    EnumStatusContestacao,
)
from chargeback.chargeback.infra.persistence.models.cliente import Cliente


class Contestacao(models.Model):
    tipo = models.SmallIntegerField(
        choices=[TIPO_CONTESTACAO],
    )
    id_transacao = models.CharField(
        verbose_name="ID da transação",
        max_length=255,
    )
    status = models.SmallIntegerField(
        verbose_name="Status da contestação",
        choices=[STATUS_CONTESTACAO],
        default=EnumStatusContestacao.ABERTO,
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    descricao = models.TextField(
        verbose_name="Descrição da contestação",
        max_length=255,
        blank=True,
        null=True,
    )
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contestação"
        verbose_name_plural = "Contestações"
