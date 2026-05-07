from abc import ABC, abstractmethod

from chargeback.domain.entities.cliente import Cliente


class IClienteRepository(ABC):

    @abstractmethod
    def obter_ou_criar(self, cliente: Cliente) -> Cliente:
        pass
