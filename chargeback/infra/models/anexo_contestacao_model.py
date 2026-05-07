from django.db import models

from chargeback.domain.value_objects.tipo_anexo import TIPO_ANEXOS
from chargeback.infra.models.contestacao_model import ContestacaoModel


class AnexoContestacaoModel(models.Model):
    contestacao = models.ForeignKey(
        ContestacaoModel,
        on_delete=models.CASCADE,
    )
    tipo = models.SmallIntegerField(
        verbose_name="Tipo do anexo",
        choices=TIPO_ANEXOS,
    )
    observacao = models.TextField(
        verbose_name="Observação",
        max_length=255,
        blank=True,
        null=True,
    )
    nome_arquivo = models.CharField(
        verbose_name="Nome do arquivo",
        max_length=255,
    )
    url = models.URLField(
        verbose_name="URL do anexo",
        max_length=255,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Anexo de Contestação"
        verbose_name_plural = "Anexos de Contestação"
