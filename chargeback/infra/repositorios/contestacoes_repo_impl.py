from chargeback.domain.entities.cliente import Cliente
from chargeback.domain.entities.contestacao import Contestacao
from chargeback.domain.repositories.icontestacao_repo import IContestacaoRepository
from chargeback.infra.models.anexo_contestacao_model import AnexoContestacaoModel
from chargeback.infra.models.cliente_model import ClienteModel
from chargeback.infra.models.contestacao_model import ContestacaoModel
from chargeback.infra.models.historico_contestacao_model import HistoricoContestacaoModel


class ContestacaoRepo(IContestacaoRepository):
    def _cliente_model_para_entidade(self, model: ClienteModel) -> Cliente:
        return Cliente(
            id=model.id,
            nome=model.nome,
            email=model.email,
            cpf=model.cpf,
            telefone=model.telefone,
            ativo=model.ativo,
        )

    def _contestacao_model_para_entidade(self, model: ContestacaoModel) -> Contestacao:
        return Contestacao(
            id=model.id,
            tipo=model.tipo,
            token_transacao=model.token_transacao,
            status=model.status,
            cliente=self._cliente_model_para_entidade(model.cliente),
            descricao=model.descricao,
            bandeira=model.bandeira,
            produto=model.produto,
            ativo=model.ativo,
            data_limite=model.data_limite,
        )

    def salvar(self, contestacao: Contestacao) -> Contestacao:
        model = ContestacaoModel.objects.create(
            tipo=contestacao.tipo,
            token_transacao=contestacao.token_transacao,
            cliente_id=contestacao.cliente.id,
            bandeira=contestacao.bandeira,
            descricao=contestacao.descricao,
            produto=contestacao.produto,
            status=contestacao.status,
            ativo=contestacao.ativo,
            data_limite=contestacao.data_limite,
        )
        return self._contestacao_model_para_entidade(model)

    def atualizar(self, contestacao: Contestacao) -> Contestacao:
        ContestacaoModel.objects.filter(id=contestacao.id, ativo=True).update(
            status=contestacao.status,
            produto=contestacao.produto,
            descricao=contestacao.descricao,
            data_limite=contestacao.data_limite,
        )
        model = ContestacaoModel.objects.select_related("cliente").get(id=contestacao.id, ativo=True)
        return self._contestacao_model_para_entidade(model)

    def listar(
        self,
        status: int | None = None,
        token_transacao: str | None = None,
        tipo: int | None = None,
    ) -> list[Contestacao]:
        query = ContestacaoModel.objects.select_related("cliente").filter(ativo=True)
        if status:
            query = query.filter(status=status)
        if token_transacao:
            query = query.filter(token_transacao=token_transacao)
        if tipo:
            query = query.filter(tipo=tipo)
        return [self._contestacao_model_para_entidade(model) for model in query.order_by("-id")]

    def deletar(self, contestacao_id: int) -> None:
        ContestacaoModel.objects.filter(id=contestacao_id).update(ativo=False)

    def buscar_por_id(self, id: int) -> Contestacao | None:
        model = ContestacaoModel.objects.select_related("cliente").filter(id=id, ativo=True).first()
        if not model:
            return None
        return self._contestacao_model_para_entidade(model)

    def buscar_por_token_transacao_tipo_contestacao(
        self,
        token_transacao: str,
        tipo_contestacao: int,
    ) -> Contestacao | None:
        model = ContestacaoModel.objects.select_related("cliente").filter(
            token_transacao=token_transacao,
            tipo=tipo_contestacao,
            ativo=True,
        ).first()
        if not model:
            return None
        return self._contestacao_model_para_entidade(model)

    def registrar_historico(self, contestacao_id, status, observacao, data_limite) -> None:
        HistoricoContestacaoModel.objects.create(
            contestacao_id=contestacao_id,
            status=status,
            observacao=observacao,
            data_limite=data_limite,
        )

    def anexar_documento(self, contestacao_id, tipo, nome_arquivo, url, observacao) -> dict:
        model = AnexoContestacaoModel.objects.create(
            contestacao_id=contestacao_id,
            tipo=tipo,
            nome_arquivo=nome_arquivo,
            url=url,
            observacao=observacao,
        )
        return {
            "id": model.id,
            "contestacao_id": model.contestacao_id,
            "tipo": model.tipo,
            "nome_arquivo": model.nome_arquivo,
            "url": model.url,
            "observacao": model.observacao,
            "criado_em": model.created_at,
        }

    def listar_anexos(self, contestacao_id: int) -> list[dict]:
        anexos = AnexoContestacaoModel.objects.filter(contestacao_id=contestacao_id).order_by("-id")
        return [
            {
                "id": model.id,
                "contestacao_id": model.contestacao_id,
                "tipo": model.tipo,
                "nome_arquivo": model.nome_arquivo,
                "url": model.url,
                "observacao": model.observacao,
                "criado_em": model.created_at,
            }
            for model in anexos
        ]
