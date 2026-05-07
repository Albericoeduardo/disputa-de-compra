from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository


class BuscarContestacaoCasoDeUso:
    def __init__(self, repo_contestacao: IContestacaoRepository):
        self.repo_contestacao = repo_contestacao

    def executar(self, contestacao_id: int):
        contestacao = self.repo_contestacao.buscar_por_id(contestacao_id)
        if not contestacao:
            return {"ok": False, "code": "NAO_ENCONTRADO", "msg": "Contestacao nao encontrada"}
        return {"ok": True, "contestacao": contestacao}
