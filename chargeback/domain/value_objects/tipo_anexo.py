from enum import IntEnum


class EnumTipoAnexos(IntEnum):
    COMPROVANTE_ENTREGA = 1
    IP_TRANSACAO = 2
    ASSINATURA_DIGITAL = 3
    REGRISTRO_COMUNICACAO = 4
    POLITICA_CANCELAMENTO = 5


TIPO_ANEXOS = (
    (EnumTipoAnexos.COMPROVANTE_ENTREGA, "Comprovante de Entrega"),
    (EnumTipoAnexos.IP_TRANSACAO, "IP da Transação"),
    (EnumTipoAnexos.ASSINATURA_DIGITAL, "Assinatura Digital"),
    (EnumTipoAnexos.REGRISTRO_COMUNICACAO, "Registro de Comunicação"),
    (EnumTipoAnexos.POLITICA_CANCELAMENTO, "Política de Cancelamento"),
)