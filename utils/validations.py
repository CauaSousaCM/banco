import re
from validate_docbr import CPF

from .messages import error_message

def validate_cpf(cpf: str, reset) -> None:
    """
    Função responsável por validar o cpf dos clientes.
    """
    cpf_instance = CPF()
    cpf_result = cpf_instance.validate(cpf)
    if cpf_result:
        pass
    else:
        print(error_message('Insira um CPF válido.'))
        reset()

def validate_email(email: str, reset=None) -> None:
    """
    Função responsável por validar o email dos clientes.
    """
    default = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(default, email) is not None:
        pass
    else:
        print(error_message('Insira um E-mail válido.'))
        reset()
