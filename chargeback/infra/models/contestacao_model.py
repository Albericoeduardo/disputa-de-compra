from django.db import models
from django.db.models import Q

from chargeback.domain.value_objects.status_contestacao import STATUS_CONTESTACAO, EnumStatusContestacao
from chargeback.domain.value_objects.tipo_contestacao import TIPO_CONTESTACAO
from chargeback.infra.models.cliente_model import ClienteModel


class ContestacaoModel(models.Model):
    tipo = models.SmallIntegerField(
        choices=TIPO_CONTESTACAO,
    )
    token_transacao = models.CharField(
        verbose_name="Token da transação",
        max_length=255,
    )
    status = models.SmallIntegerField(
        verbose_name="Status da contestação",
        choices=STATUS_CONTESTACAO,
        default=EnumStatusContestacao.ABERTO,
    )
    cliente = models.ForeignKey(
        ClienteModel,
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
    data_limite = models.DateTimeField(
        verbose_name="Data limite da etapa",
        blank=True,
        null=True,
    )
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contestacao {self.id} - tipo {self.tipo} - token {self.token_transacao}"

    class Meta:
        verbose_name = "Contestação"
        verbose_name_plural = "Contestações"
