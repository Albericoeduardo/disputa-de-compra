from django.db import models

from chargeback.domain.value_objects.status_contestacao import STATUS_CONTESTACAO


class PrazoEtapaModel(models.Model):
    bandeira = models.CharField(max_length=50)
    status = models.SmallIntegerField(choices=STATUS_CONTESTACAO)
    dias_prazo = models.PositiveSmallIntegerField()
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Prazo por Etapa"
        verbose_name_plural = "Prazos por Etapa"
        constraints = [
            models.UniqueConstraint(
                fields=["bandeira", "status"],
                condition=models.Q(ativo=True),
                name="uniq_prazo_bandeira_status_ativo",
            ),
        ]
