from chargeback.chargeback.domain.aggregates.contestacao_aggr import ContestacaoAggregate
from chargeback.chargeback.domain.repositories.contestacao_repo import (
    AbcstractContestacaoRepo,
)
from chargeback.chargeback.infra.models.contestacao import Contestacao


class ContestacaoRepo(AbcstractContestacaoRepo):

    def salvar(self, contestacao) -> None:
        model = Contestacao.objects.create(
            tipo=contestacao.tipo,
            token_transacao=contestacao.token_transacao,
            cliente=contestacao.cliente,
            bandeira=contestacao.bandeira,
            descricao=contestacao.descricao,
            produto=contestacao.produto,
        )
        contestacao.id = model.id
        return contestacao

    def buscar_por_token_transacao_tipo_contestacao(
        self,
        token_transacao: str,
        tipo_contestacao: int
    ) -> Contestacao:
        try:
            model = Contestacao.objects.get(
                token_transacao=token_transacao,
                tipo=tipo_contestacao,
                ativo=True,
            )
            return ContestacaoAggregate(
                id=model.id,
                tipo=model.tipo,
                token_transacao=model.token_transacao,
                status=model.status,
                cliente=model.cliente,
                descricao=model.descricao,
                bandeira=model.bandeira,
                produto=model.produto,
            )
        except Contestacao.DoesNotExist:
            return None