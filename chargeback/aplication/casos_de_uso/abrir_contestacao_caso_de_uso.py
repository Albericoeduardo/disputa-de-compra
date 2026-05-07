from chargeback.domain.entities.cliente import Cliente
from chargeback.domain.entities.contestacao import Contestacao
from chargeback.domain.repositories.icliente_repo import IClienteRepository
from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository
from chargeback.domain.services.prazo_service import PrazoService
from chargeback.domain.services.contestacao_service import ContestacaoService
from chargeback.domain.value_objects.status_contestacao import EnumStatusContestacao


class AbrirContestacaoCasoDeUso:
    def __init__(
        self,
        repo_contestacao: IContestacaoRepository,
        repo_cliente: IClienteRepository,
        unicidade_service: ContestacaoService,
        prazo_service: PrazoService,
    ):
        self.repo_contestacao = repo_contestacao
        self.repo_cliente = repo_cliente
        self.unicidade_service = unicidade_service
        self.prazo_service = prazo_service

    def executar(self, contestacao_dto: dict):
        tipo = contestacao_dto["tipo_contestacao"]
        token_transacao = contestacao_dto["token_transacao"]

        pode_abrir, mensagem = self.unicidade_service.pode_abrir_contestacao(
            tipo=tipo,
            token_transacao=token_transacao,
        )
        if not pode_abrir:
            return {"ok": False, "code": "CONTESTACAO_DUPLICADA", "msg": mensagem}

        cliente_payload = contestacao_dto["cliente"]
        cliente = Cliente(
            id=None,
            nome=cliente_payload["nome"],
            email=cliente_payload["email"],
            cpf=cliente_payload["cpf"],
            telefone=cliente_payload.get("telefone"),
        )
        cliente = self.repo_cliente.obter_ou_criar(cliente)

        data_limite = self.prazo_service.calcular_data_limite(
            bandeira=contestacao_dto["bandeira"],
            status=EnumStatusContestacao.ABERTO,
        )

        contestacao = Contestacao.abrir(
            tipo=tipo,
            token_transacao=token_transacao,
            cliente=cliente,
            bandeira=contestacao_dto["bandeira"],
            data_limite=data_limite,
            produto=contestacao_dto.get("produto"),
            descricao=contestacao_dto.get("descricao"),
        )

        contestacao_criada = self.repo_contestacao.salvar(contestacao)
        self.repo_contestacao.registrar_historico(
            contestacao_id=contestacao_criada.id,
            status=contestacao_criada.status,
            observacao="Contestacao aberta",
            data_limite=contestacao_criada.data_limite,
        )

        return {"ok": True, "contestacao": contestacao_criada}
