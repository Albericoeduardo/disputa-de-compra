from enum import IntEnum


class EnumStatusContestacao(IntEnum):
    ABERTO = 1
    EM_ANALISE = 2
    EM_DISPUTA = 3
    REABERTO = 4
    ENCERRADO_COM_PERDA = 5
    ENCERRADO_COM_GANHO = 6


STATUS_CONTESTACAO = (
    (EnumStatusContestacao.ABERTO, "Aberto"),
    (EnumStatusContestacao.EM_ANALISE, "Em Análise"),
    (EnumStatusContestacao.EM_DISPUTA, "Em Disputa"),
    (EnumStatusContestacao.REABERTO, "Reaberto"),
    (EnumStatusContestacao.ENCERRADO_COM_PERDA, "Encerrado com Perda"),
    (EnumStatusContestacao.ENCERRADO_COM_GANHO, "Encerrado com Ganho"),
)