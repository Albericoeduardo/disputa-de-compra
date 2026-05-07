from chargeback.domain.exceptions import DomainError
from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository
from chargeback.domain.services.prazo_service import PrazoService


class AtualizarStatusContestacaoCasoDeUso:
    def __init__(
        self,
        repo_contestacao: IContestacaoRepository,
        prazo_service: PrazoService,
    ):
        self.repo_contestacao = repo_contestacao
        self.prazo_service = prazo_service

    def executar(self, contestacao_id: int, novo_status: int, observacao: str | None = None):
        contestacao = self.repo_contestacao.buscar_por_id(contestacao_id)
        if not contestacao:
            return {"ok": False, "code": "NAO_ENCONTRADO", "msg": "Contestacao nao encontrada"}

        nova_data_limite = self.prazo_service.calcular_data_limite(
            bandeira=contestacao.bandeira,
            status=novo_status,
        )

        try:
            contestacao.transicionar_para(
                novo_status=novo_status,
                nova_data_limite=nova_data_limite,
                agora=self.prazo_service.agora_utc(),
            )
        except DomainError as erro:
            return {"ok": False, "code": "TRANSICAO_INVALIDA", "msg": str(erro)}

        contestacao_atualizada = self.repo_contestacao.atualizar(contestacao)
        self.repo_contestacao.registrar_historico(
            contestacao_id=contestacao_atualizada.id,
            status=contestacao_atualizada.status,
            observacao=observacao,
            data_limite=contestacao_atualizada.data_limite,
        )
        return {"ok": True, "contestacao": contestacao_atualizada}
