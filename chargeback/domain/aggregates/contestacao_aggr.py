from dataclasses import dataclass

from chargeback.chargeback.infra.models.anexo_contestacao import AnexoContestacao
from chargeback.chargeback.infra.models.cliente import Cliente


@dataclass(frozen=True)
class ContestacaoAggregate:
    tipo: int
    token_transacao: str
    status: int
    cliente: Cliente
    descricao: str
    bandeira: str
    evidencias: list[AnexoContestacao] | None = None
    produto: str | None = None
