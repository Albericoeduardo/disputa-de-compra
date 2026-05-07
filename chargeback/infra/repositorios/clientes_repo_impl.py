from chargeback.domain.entities.cliente import Cliente
from chargeback.domain.repositories.icliente_repo import IClienteRepository
from chargeback.infra.models.cliente_model import ClienteModel


class ClienteRepo(IClienteRepository):
    def obter_ou_criar(self, cliente: Cliente) -> Cliente:
        model, created = ClienteModel.objects.get_or_create(
            cpf=cliente.cpf,
            defaults={
                "nome": cliente.nome,
                "email": cliente.email,
                "telefone": cliente.telefone,
                "ativo": True,
            },
        )

        if not created:
            alterado = False
            if model.nome != cliente.nome:
                model.nome = cliente.nome
                alterado = True
            if model.email != cliente.email:
                model.email = cliente.email
                alterado = True
            if model.telefone != cliente.telefone:
                model.telefone = cliente.telefone
                alterado = True
            if not model.ativo:
                model.ativo = True
                alterado = True
            if alterado:
                model.save(update_fields=["nome", "email", "telefone", "ativo"])

        return Cliente(
            id=model.id,
            nome=model.nome,
            email=model.email,
            cpf=model.cpf,
            telefone=model.telefone,
            ativo=model.ativo,
        )
