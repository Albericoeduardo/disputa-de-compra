from chargeback.chargeback.domain.aggregates.contestacao_aggr import ContestacaoAggregate
from chargeback.chargeback.domain.repositories.contestacao_repo import (
    AbcstractContestacaoRepo,
)
from chargeback.chargeback.infra.persistence.models.contestacao import Contestacao


class ContestacoesRepo(AbcstractContestacaoRepo):

    def salvar(self, contestacao: Contestacao) -> None:
        model = Contestacao.objects.create(
            tipo=contestacao.tipo,
            cliente=contestacao.cliente,
            descricao=contestacao.descricao,
        )
        contestacao.id = model.id
        return contestacao
    
    def buscar_por_id_transacao_tipo_contestacao(
        self,
        id_transacao: str,
        tipo_contestacao: int
    ) -> Contestacao:
        try:
            model = Contestacao.objects.get(
                id_transacao=id_transacao,
                tipo=tipo_contestacao,
                ativo=True,
            )
            return ContestacaoAggregate(
                id=model.id,
                tipo=model.tipo,
                id_transacao=model.id_transacao,
                status=model.status,
                cliente=model.cliente,
                descricao=model.descricao,
            )
        except Contestacao.DoesNotExist:
            return None