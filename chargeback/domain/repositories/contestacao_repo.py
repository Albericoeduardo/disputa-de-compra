from abc import ABC, abstractmethod

from chargeback.chargeback.infra.models.contestacao import Contestacao


class AbcstractContestacaoRepo(ABC):

    @abstractmethod
    def salvar(self, contestacao: Contestacao) -> None:
        pass

    @abstractmethod
    def buscar_por_token_transacao_tipo_contestacao(self, token_transacao: str, tipo_contestacao: int) -> Contestacao:
        pass
