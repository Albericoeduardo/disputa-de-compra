from chargeback.domain.exceptions import DomainError
from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository


class AnexarDocumentoCasoDeUso:
    def __init__(self, repo_contestacao: IContestacaoRepository):
        self.repo_contestacao = repo_contestacao

    def executar(
        self,
        contestacao_id: int,
        tipo: int,
        nome_arquivo: str,
        url: str,
        observacao: str | None = None,
    ):
        contestacao = self.repo_contestacao.buscar_por_id(contestacao_id)
        if not contestacao:
            return {"ok": False, "code": "NAO_ENCONTRADO", "msg": "Contestacao nao encontrada"}

        try:
            contestacao.validar_recebimento_anexo()
        except DomainError as erro:
            return {
                "ok": False,
                "code": "STATUS_INVALIDO",
                "msg": str(erro),
            }

        anexo = self.repo_contestacao.anexar_documento(
            contestacao_id=contestacao_id,
            tipo=tipo,
            nome_arquivo=nome_arquivo,
            url=url,
            observacao=observacao,
        )
        return {"ok": True, "anexo": anexo}
