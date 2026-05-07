class DomainError(Exception):
    pass


class InvarianteContestacaoError(DomainError):
    pass


class TransicaoStatusInvalidaError(DomainError):
    pass


class PrazoExpiradoError(DomainError):
    pass


class ContestacaoNaoAceitaAnexoError(DomainError):
    pass
