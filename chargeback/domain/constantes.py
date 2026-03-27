from enum import IntEnum


class EnumTipoContestacao(IntEnum):
    NAO_RECONHECIMENTO = 1
    PRODUTO_NAO_ENTREGUE = 2
    PRODUTO_DIVERGENTE = 3
    CANCELAMENTO_NAO_PROCESSADO = 4
    COBRANCA_DUPLICADA = 5


class EnumStatusContestacao(IntEnum):
    ABERTO = 1
    EM_ANALISE = 2
    EM_DISPUTA = 3
    REABERTO = 4
    ENCERRADO_COM_PERDA = 5
    ENCERRADO_COM_GANHO = 6


class EnumTipoAnexos(IntEnum):
    COMPROVANTE_ENTREGA = 1
    IP_TRANSACAO = 2
    ASSINATURA_DIGITAL = 3
    REGRISTRO_COMUNICACAO = 4
    POLITICA_CANCELAMENTO = 5


TIPO_CONTESTACAO = (
    (EnumTipoContestacao.NAO_RECONHECIMENTO, "Não Reconhecimento"),
    (EnumTipoContestacao.PRODUTO_NAO_ENTREGUE, "Produto Não Entregue"),
    (EnumTipoContestacao.PRODUTO_DIVERGENTE, "Produto Divergente"),
    (EnumTipoContestacao.CANCELAMENTO_NAO_PROCESSADO, "Cancelamento Não Processado"),
    (EnumTipoContestacao.COBRANCA_DUPLICADA, "Cobrança Duplicada"),
)


STATUS_CONTESTACAO = (
    (EnumStatusContestacao.ABERTO, "Aberto"),
    (EnumStatusContestacao.EM_ANALISE, "Em Análise"),
    (EnumStatusContestacao.EM_DISPUTA, "Em Disputa"),
    (EnumStatusContestacao.REABERTO, "Reaberto"),
    (EnumStatusContestacao.ENCERRADO_COM_PERDA, "Encerrado com Perda"),
    (EnumStatusContestacao.ENCERRADO_COM_GANHO, "Encerrado com Ganho"),
)


TIPO_ANEXOS = (
    (EnumTipoAnexos.COMPROVANTE_ENTREGA, "Comprovante de Entrega"),
    (EnumTipoAnexos.IP_TRANSACAO, "IP da Transação"),
    (EnumTipoAnexos.ASSINATURA_DIGITAL, "Assinatura Digital"),
    (EnumTipoAnexos.REGRISTRO_COMUNICACAO, "Registro de Comunicação"),
    (EnumTipoAnexos.POLITICA_CANCELAMENTO, "Política de Cancelamento"),
)
