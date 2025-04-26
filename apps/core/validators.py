import re
from django.core.exceptions import ValidationError

def validar_placa(value):
    """
    Valida se a placa está no formato brasileiro (antigo ou Mercosul).
    Lança ValidationError se inválido.
    """
    placa_antiga = re.compile(r'^[A-Z]{3}-\d{4}$')
    placa_mercosul = re.compile(r'^[A-Z]{3}\d[A-Z]\d{2}$')

    if not (placa_antiga.match(value) or placa_mercosul.match(value)):
        raise ValidationError(
            'Placa inválida. Use o formato ABC-1234 ou ABC1D23.',
            code='invalid_plate'
        )

def validar_cnpj(value):
    """
    Valida se o CNPJ informado possui 14 dígitos numéricos.
    """
    cnpj = re.sub(r'\D','', value) # Remove tudo que não for número
    if len(cnpj) != 14:
        raise ValidationError('CNPJ deve conter 14 dígitos númericos.')