from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository


class ListarContestacoesCasoDeUso:
    def __init__(self, repo_contestacao: IContestacaoRepository):
        self.repo_contestacao = repo_contestacao

    def executar(
        self,
        status: int | None = None,
        token_transacao: str | None = None,
        tipo: int | None = None,
    ):
        contestacoes = self.repo_contestacao.listar(
            status=status,
            token_transacao=token_transacao,
            tipo=tipo,
        )
        return {"ok": True, "contestacoes": contestacoes}
