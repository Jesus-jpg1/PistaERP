import uuid
from datetime import datetime
import random
import string

def gerar_uuid():
    """Gera um UUID único como string, útil pra códigos públicos."""
    return str(uuid.uuid4())

def formatar_data_br(data: datetime) -> str:
    """Formata uma data no formato brasileiro dd/mm/aaaa."""
    return data.strftime('%d/%m/%Y')

def formatar_valor(valor: float) -> str:
    """Formata um valor decimal em reais."""
    return f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

def gerar_placa(tipo='aleatorio'):
    """
    Gera uma placa válida brasileira.
    
    tipo:
      - 'antiga' -> padrão AAA-1234
      - 'mercosul' -> padrão ABC1D23
      - 'aleatorio' -> escolhe entre os dois
    """
    if tipo == 'antiga':
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        numeros = ''.join(random.choices(string.digits, k=4))
        return f"{letras}-{numeros}"
    
    elif tipo == 'mercosul':
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        digito1 = random.choice(string.digits)
        letra4 = random.choice(string.ascii_uppercase)
        digitos_finais = ''.join(random.choices(string.digits, k=2))
        return f"{letras}{digito1}{letra4}{digitos_finais}"
    
    else:
        return gerar_placa(random.choice(['antiga', 'mercosul']))