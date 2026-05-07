class Cliente:
    def __init__(
            self,
            nome: str,
            email: str,
            cpf: str,
            telefone: str | None,
            id: int | None = None,
            ativo: bool = True,
        ):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.ativo = ativo
