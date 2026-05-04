from chargeback.domain.entities.contestacao import Contestacao
from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository
from chargeback.domain.value_objects.status_contestacao import EnumStatusContestacao
from chargeback.infra.models.contestacao_model import ContestacaoModel


class ContestacaoRepo(IContestacaoRepository):

    def salvar(self, contestacao: Contestacao):
        model = ContestacaoModel.objects.create(
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
            model = ContestacaoModel.objects.get(
                token_transacao=token_transacao,
                tipo=tipo_contestacao,
                status=EnumStatusContestacao.ABERTO,
                ativo=True,
            )
            return Contestacao(
                id=model.id,
                tipo=model.tipo,
                token_transacao=model.token_transacao,
                status=model.status,
                cliente=model.cliente,
                descricao=model.descricao,
                bandeira=model.bandeira,
                produto=model.produto,
            )
        except ContestacaoModel.DoesNotExist:
            return None