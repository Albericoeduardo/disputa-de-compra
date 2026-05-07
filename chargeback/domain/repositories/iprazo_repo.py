from abc import ABC, abstractmethod


class IPrazoRepository(ABC):

    @abstractmethod
    def buscar_dias_por_bandeira_e_status(self, bandeira: str, status: int) -> int | None:
        pass
