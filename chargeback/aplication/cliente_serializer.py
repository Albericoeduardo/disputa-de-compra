from rest_framework import serializers


class ClienteSerializer(serializers.Serializer):
    nome = serializers.CharField(required=True, help_text="Nome do cliente")
    email = serializers.EmailField(required=True, help_text="Email do cliente")
    cpf = serializers.CharField(required=True, help_text="CPF do cliente")
    telefone = serializers.CharField(required=False, help_text="Telefone do cliente")