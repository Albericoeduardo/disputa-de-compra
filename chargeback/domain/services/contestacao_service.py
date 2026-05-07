from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository


class ContestacaoService:
    def __init__(
        self,
        contestacao_repo: IContestacaoRepository,
    ):
        self.contestacao_repo = contestacao_repo

    def pode_abrir_contestacao(
        self,
        tipo: int,
        token_transacao: str
    ) -> tuple[bool, str]:
        """
        Valida se é possível abrir uma contestação.

        Regra de negócio: Não pode haver contestação do mesmo tipo
        para a mesma transação.

        :param tipo: Tipo da contestação
        :param token_transacao: Token da transação
        :return: Tuple indicando se é possível abrir a contestação e mensagem explicativa
        """
        contestacao_existente = self.contestacao_repo.buscar_por_token_transacao_tipo_contestacao(
            token_transacao=token_transacao,
            tipo=tipo,
        )

        if contestacao_existente:
            return False, f"Já existe uma contestação desse tipo: {tipo} para esta transação"

        return True, "OK"

