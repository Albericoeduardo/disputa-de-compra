from chargeback.chargeback.infra.models.contestacao import Contestacao
from chargeback.chargeback.infra.repositorios.contestacoes_repo_impl import (
    ContestacaoRepo,
)


class AbrirContestacaoCasoDeUso:
    def __init__(self, repo_contestacao: ContestacaoRepo):
        self.repo_contestacao = repo_contestacao

    def executar(self, contestacao):
        try:
            self.repo_contestacao.buscar_por_token_transacao_tipo_contestacao(
                contestacao.token_transacao, contestacao.tipo
            )
            return {"msg": "Já existe uma contestação desse tipo para essa transação"}
        except Exception:
            raise
        except Contestacao.DoesNotExist:
            return self.repo_contestacao.salvar(contestacao)
