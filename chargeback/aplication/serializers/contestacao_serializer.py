from rest_framework import serializers

from chargeback.aplication.serializers.cliente_serializer import ClienteSerializer
from chargeback.domain.value_objects.status_contestacao import EnumStatusContestacao
from chargeback.domain.value_objects.tipo_contestacao import EnumTipoContestacao


class ContestacaoViewSerializer(serializers.Serializer):
    tipo_contestacao = serializers.ChoiceField(
        required=True,
        choices=[(item.value, item.name) for item in EnumTipoContestacao],
        help_text="Tipo da contestacao",
    )
    token_transacao = serializers.CharField(required=True, help_text="Token da transação")
    produto = serializers.CharField(required=False, help_text="Produto relacionado à contestação")
    bandeira = serializers.CharField(required=True, help_text="Bandeira do cartão")
    descricao = serializers.CharField(required=False, help_text="Descrição da contestação")
    cliente = ClienteSerializer(required=True, help_text="Dados do cliente")


class AtualizarStatusContestacaoSerializer(serializers.Serializer):
    status = serializers.ChoiceField(
        required=True,
        choices=[(item.value, item.name) for item in EnumStatusContestacao],
        help_text="Novo status da contestacao",
    )
    observacao = serializers.CharField(required=False, allow_blank=True)


class FiltroContestacaoSerializer(serializers.Serializer):
    status = serializers.IntegerField(required=False)
    token_transacao = serializers.CharField(required=False)
    tipo = serializers.IntegerField(required=False)


class ClienteOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField()
    email = serializers.EmailField()
    cpf = serializers.CharField()
    telefone = serializers.CharField(allow_null=True, allow_blank=True, required=False)


class ContestacaoOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tipo = serializers.IntegerField()
    token_transacao = serializers.CharField()
    status = serializers.IntegerField()
    bandeira = serializers.CharField()
    produto = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    descricao = serializers.CharField(allow_null=True, allow_blank=True, required=False)
    data_limite = serializers.DateTimeField(allow_null=True)
    cliente = ClienteOutputSerializer()

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "tipo": instance.tipo,
            "token_transacao": instance.token_transacao,
            "status": instance.status,
            "bandeira": instance.bandeira,
            "produto": instance.produto,
            "descricao": instance.descricao,
            "data_limite": instance.data_limite,
            "cliente": {
                "id": instance.cliente.id,
                "nome": instance.cliente.nome,
                "email": instance.cliente.email,
                "cpf": instance.cliente.cpf,
                "telefone": instance.cliente.telefone,
            },
        }
