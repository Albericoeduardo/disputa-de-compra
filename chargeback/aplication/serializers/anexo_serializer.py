from rest_framework import serializers

from chargeback.domain.value_objects.tipo_anexo import EnumTipoAnexos


class AnexoContestacaoSerializer(serializers.Serializer):
    tipo = serializers.ChoiceField(
        required=True,
        choices=[(item.value, item.name) for item in EnumTipoAnexos],
        help_text="Tipo da evidencia",
    )
    nome_arquivo = serializers.CharField(required=True)
    url = serializers.URLField(required=True)
    observacao = serializers.CharField(required=False, allow_blank=True)
