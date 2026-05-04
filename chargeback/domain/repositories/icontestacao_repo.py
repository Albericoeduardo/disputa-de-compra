from abc import ABC, abstractmethod

from chargeback.domain.entities.contestacao import Contestacao


class IContestacaoRepository(ABC):

    @abstractmethod
    def salvar(self, contestacao: Contestacao) -> Contestacao:
        pass

    @abstractmethod
    def atualizar(self, contestacao: Contestacao) -> None:
        pass

    @abstractmethod
    def listar(self) -> list[Contestacao]:
        pass

    @abstractmethod
    def deletar(self, contestacao: Contestacao) -> None:
        pass
    
    @abstractmethod
    def buscar_por_id(self, id: int) -> Contestacao:
        pass
    
    @abstractmethod
    def buscar_por_token_transacao_tipo_contestacao(self, token_transacao: str, tipo_contestacao: int) -> Contestacao:
        pass
