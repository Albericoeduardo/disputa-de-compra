from chargeback.domain.repositories.iprazo_repo import IPrazoRepository
from chargeback.infra.models.prazo_etapa_model import PrazoEtapaModel


class PrazoRepo(IPrazoRepository):
    def buscar_dias_por_bandeira_e_status(self, bandeira: str, status: int) -> int | None:
        model = PrazoEtapaModel.objects.filter(
            bandeira=bandeira,
            status=status,
            ativo=True,
        ).first()
        return int(model.dias_prazo)
