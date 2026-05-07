from abc import ABC, abstractmethod
from datetime import datetime

from chargeback.domain.entities.contestacao import Contestacao


class IContestacaoRepository(ABC):

    @abstractmethod
    def salvar(self, contestacao: Contestacao) -> Contestacao:
        pass

    @abstractmethod
    def atualizar(self, contestacao: Contestacao) -> Contestacao:
        pass

    @abstractmethod
    def listar(
        self,
        status: int | None = None,
        token_transacao: str | None = None,
        tipo: int | None = None,
    ) -> list[Contestacao]:
        pass

    @abstractmethod
    def deletar(self, contestacao_id: int) -> None:
        pass
    
    @abstractmethod
    def buscar_por_id(self, id: int) -> Contestacao | None:
        pass
    
    @abstractmethod
    def buscar_por_token_transacao_tipo_contestacao(
        self,
        token_transacao: str,
        tipo_contestacao: int,
    ) -> Contestacao | None:
        pass

    @abstractmethod
    def registrar_historico(
        self,
        contestacao_id: int,
        status: int,
        observacao: str | None,
        data_limite: datetime | None,
    ) -> None:
        pass

    @abstractmethod
    def anexar_documento(
        self,
        contestacao_id: int,
        tipo: int,
        nome_arquivo: str,
        url: str,
        observacao: str | None,
    ) -> dict:
        pass

    @abstractmethod
    def listar_anexos(self, contestacao_id: int) -> list[dict]:
        pass
