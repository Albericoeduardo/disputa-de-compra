from datetime import UTC, datetime

from chargeback.domain.entities.cliente import Cliente
from chargeback.domain.exceptions import (
    ContestacaoNaoAceitaAnexoError,
    InvarianteContestacaoError,
    PrazoExpiradoError,
    TransicaoStatusInvalidaError,
)
from chargeback.domain.value_objects.status_contestacao import EnumStatusContestacao


class Contestacao:
    _TRANSICOES_VALIDAS = {
        EnumStatusContestacao.ABERTO: {EnumStatusContestacao.EM_ANALISE},
        EnumStatusContestacao.EM_ANALISE: {
            EnumStatusContestacao.EM_DISPUTA,
            EnumStatusContestacao.ENCERRADO_COM_GANHO,
            EnumStatusContestacao.ENCERRADO_COM_PERDA,
        },
        EnumStatusContestacao.EM_DISPUTA: {
            EnumStatusContestacao.ENCERRADO_COM_GANHO,
            EnumStatusContestacao.ENCERRADO_COM_PERDA,
        },
        EnumStatusContestacao.REABERTO: {EnumStatusContestacao.EM_ANALISE},
        EnumStatusContestacao.ENCERRADO_COM_GANHO: set(),
        EnumStatusContestacao.ENCERRADO_COM_PERDA: set(),
    }

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
        data_limite: datetime | None = None,
    ):
        if tipo is None:
            raise InvarianteContestacaoError("Tipo da contestacao e obrigatorio")
        if not token_transacao:
            raise InvarianteContestacaoError("Token da transacao e obrigatorio")
        if cliente is None:
            raise InvarianteContestacaoError("Cliente e obrigatorio")
        if not bandeira:
            raise InvarianteContestacaoError("Bandeira e obrigatoria")

        self._id = id
        self._tipo = tipo
        self._token_transacao = token_transacao
        self._status = status
        self._cliente = cliente
        self._ativo = ativo
        self._bandeira = bandeira
        self._produto = produto
        self._descricao = descricao
        self._data_limite = data_limite

    @classmethod
    def abrir(
        cls,
        tipo: int,
        token_transacao: str,
        cliente: Cliente,
        bandeira: str,
        data_limite: datetime | None,
        produto: str | None = None,
        descricao: str | None = None,
    ) -> "Contestacao":
        return cls(
            tipo=tipo,
            token_transacao=token_transacao,
            cliente=cliente,
            bandeira=bandeira,
            status=EnumStatusContestacao.ABERTO,
            data_limite=data_limite,
            produto=produto,
            descricao=descricao,
        )

    @property
    def id(self) -> int | None:
        return self._id

    @id.setter
    def id(self, value: int | None):
        self._id = value

    @property
    def tipo(self) -> int:
        return self._tipo

    @property
    def token_transacao(self) -> str:
        return self._token_transacao

    @property
    def status(self) -> int:
        return self._status

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def ativo(self) -> bool:
        return self._ativo

    @property
    def bandeira(self) -> str:
        return self._bandeira

    @property
    def produto(self) -> str | None:
        return self._produto

    @property
    def descricao(self) -> str | None:
        return self._descricao

    @property
    def data_limite(self) -> datetime | None:
        return self._data_limite

    def esta_expirada(self, agora: datetime | None = None) -> bool:
        if self._data_limite is None:
            return False
        referencia = agora or datetime.now(UTC)
        return referencia > self._data_limite

    def pode_receber_anexo(self, agora: datetime | None = None) -> bool:
        if self._status in {
            EnumStatusContestacao.ENCERRADO_COM_GANHO,
            EnumStatusContestacao.ENCERRADO_COM_PERDA,
        }:
            return False
        if self.esta_expirada(agora=agora):
            return False
        return True

    def validar_recebimento_anexo(self, agora: datetime | None = None) -> None:
        if not self.pode_receber_anexo(agora=agora):
            raise ContestacaoNaoAceitaAnexoError(
                "Contestacao nao pode receber anexo no estado atual"
            )

    def transicionar_para(
        self,
        novo_status: int,
        nova_data_limite: datetime | None,
        agora: datetime | None = None,
    ) -> None:
        if self.esta_expirada(agora=agora):
            raise PrazoExpiradoError("Nao e possivel transicionar: prazo expirado")

        permitidos = self._TRANSICOES_VALIDAS.get(self._status, set())
        if novo_status not in permitidos:
            raise TransicaoStatusInvalidaError(
                "Transicao de status invalida para a etapa atual"
            )

        self._status = novo_status
        self._data_limite = nova_data_limite
