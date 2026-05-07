from datetime import UTC, datetime, timedelta

from chargeback.domain.repositories.iprazo_repo import IPrazoRepository
from chargeback.domain.value_objects.status_contestacao import EnumStatusContestacao


class PrazoService:
    def __init__(self, prazo_repo: IPrazoRepository):
        self.prazo_repo = prazo_repo

    def calcular_data_limite(
        self,
        bandeira: str,
        status: int,
    ) -> datetime | None:
        """
        Retorna a nova data limite com base na bandeira e status.
        
        :param bandeira: A bandeira da transação (ex: Visa, Mastercard).
        :param status: O novo status da contestação.
        :return: A nova data limite ou None se o status for de encerramento.
        """
        if status in {
            EnumStatusContestacao.ENCERRADO_COM_GANHO,
            EnumStatusContestacao.ENCERRADO_COM_PERDA,
        }:
            return None

        dias = self.prazo_repo.buscar_dias_por_bandeira_e_status(bandeira=bandeira, status=status)
        base = datetime.now(UTC)
        return base + timedelta(days=dias)
