from django.db import models

from chargeback.chargeback.domain.constantes import TIPO_ANEXOS
from chargeback.chargeback.infra.models.contestacao import Contestacao


class AnexoContestacao(models.Model):
    contestacao = models.ForeignKey(
        Contestacao,
        on_delete=models.CASCADE,
    )
    tipo = models.SmallIntegerField(
        verbose_name="Tipo do anexo",
        choices=TIPO_ANEXOS,
    )
    url = models.URLField(
        verbose_name="URL do anexo",
        max_length=255,
    )
    observacao = models.TextField(
        verbose_name="Observação",
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Anexo de Contestação"
        verbose_name_plural = "Anexos de Contestação"
