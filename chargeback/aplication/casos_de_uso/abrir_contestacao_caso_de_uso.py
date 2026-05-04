from chargeback.domain.entities.contestacao import Contestacao
from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository
from chargeback.domain.services.contestacao_service import ContestacaoService


class AbrirContestacaoCasoDeUso:
    def __init__(
            self,
            repo_contestacao: IContestacaoRepository,
            validacao_service: ContestacaoService,
        ):
        self.repo_contestacao = repo_contestacao
        self.validacao_service = validacao_service

    def executar(self, contestacao_dto):
        pode_abrir, mensagem = self.validacao_service.pode_abrir_contestacao(
            tipo=contestacao_dto.tipo,
            token_transacao=contestacao_dto.token_transacao,
        )

        if not pode_abrir:
            return {"msg": mensagem}

        contestacao = Contestacao(
            tipo=contestacao_dto.tipo,
            token_transacao=contestacao_dto.token_transacao,
            cliente_id=contestacao_dto.cliente_id,
            bandeira=contestacao_dto.bandeira,
            produto=contestacao_dto.produto,
            descricao=contestacao_dto.descricao,
        )

        return self.repo_contestacao.salvar(contestacao)
