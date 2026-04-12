from rest_framework import serializers

from chargeback.chargeback.aplication.cliente_serializer import ClienteSerializer


class ContestacaoViewSerializer(serializers.Serializer):
    tipo_contestacao = serializers.IntegerField(required=True, help_text="Tipo da contestação")
    token_transacao = serializers.CharField(required=True, help_text="Token da transação")
    produto = serializers.CharField(required=False, help_text="Produto relacionado à contestação")
    bandeira = serializers.CharField(required=True, help_text="Bandeira do cartão")
    descricao = serializers.CharField(required=False, help_text="Descrição da contestação")
    cliente = ClienteSerializer(required=True, help_text="Dados do cliente")