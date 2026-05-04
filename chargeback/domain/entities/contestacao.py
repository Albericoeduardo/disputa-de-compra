from chargeback.domain.entities.cliente import Cliente
from chargeback.domain.value_objects.status_contestacao import EnumStatusContestacao


class Contestacao:
    def __init__(
        self,
        tipo: int,
        token_transacao: str,
        cliente: Cliente,
        bandeira: str,
        ativo: bool = True,
        status: int = EnumStatusContestacao.ABERTO,
        id: int | None = None,
        produto: str | None = None,
        descricao: str | None = None,
    ):
        self.id = id
        self.tipo = tipo
        self.token_transacao = token_transacao
        self.status = status
        self.cliente = cliente
        self.ativo = ativo
        self.bandeira = bandeira
        self.produto = produto
        self.descricao = descricao
