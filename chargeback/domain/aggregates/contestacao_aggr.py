from dataclasses import dataclass

from chargeback.chargeback.infra.persistence.models.cliente import Cliente


@dataclass(frozen=True)
class ContestacaoAggregate:
    tipo: int
    cliente: Cliente
    descricao: str
