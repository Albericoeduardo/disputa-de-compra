from django.db import models

from chargeback.chargeback.domain.constantes import (
    STATUS_CONTESTACAO,
    TIPO_CONTESTACAO,
    EnumStatusContestacao,
)
from chargeback.chargeback.infra.models.cliente import Cliente


class Contestacao(models.Model):
    tipo = models.SmallIntegerField(
        choices=[TIPO_CONTESTACAO],
    )
    token_transacao = models.CharField(
        verbose_name="Token da transação",
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
    produto = models.CharField(
        verbose_name="Produto",
        max_length=255,
        blank=True,
        null=True,
    )
    bandeira = models.CharField(
        verbose_name="Bandeira do cartão",
        max_length=255,
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
