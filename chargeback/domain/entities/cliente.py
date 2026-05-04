class Cliente:
    def __init__(
            self,
            nome: str,
            email: str,
            cpf: str,
            telefone: str,
            ativo: bool = True,
        ):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.ativo = ativo
