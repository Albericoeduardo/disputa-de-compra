from abc import ABC, abstractmethod

from chargeback.chargeback.infra.persistence.models.contestacao import Contestacao


class AbcstractContestacaoRepo(ABC):

    @abstractmethod
    def salvar(self, contestacao: Contestacao) -> None:
        pass

    @abstractmethod
    def buscar_por_id_transacao_tipo_contestacao(self, id_transacao: int, tipo_contestacao: int) -> Contestacao:
        pass
