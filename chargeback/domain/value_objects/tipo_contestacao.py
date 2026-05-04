from enum import IntEnum


class EnumTipoContestacao(IntEnum):
    NAO_RECONHECIMENTO = 1
    PRODUTO_NAO_ENTREGUE = 2
    PRODUTO_DIVERGENTE = 3
    CANCELAMENTO_NAO_PROCESSADO = 4
    COBRANCA_DUPLICADA = 5


TIPO_CONTESTACAO = (
    (EnumTipoContestacao.NAO_RECONHECIMENTO, "Não Reconhecimento"),
    (EnumTipoContestacao.PRODUTO_NAO_ENTREGUE, "Produto Não Entregue"),
    (EnumTipoContestacao.PRODUTO_DIVERGENTE, "Produto Divergente"),
    (EnumTipoContestacao.CANCELAMENTO_NAO_PROCESSADO, "Cancelamento Não Processado"),
    (EnumTipoContestacao.COBRANCA_DUPLICADA, "Cobrança Duplicada"),
)