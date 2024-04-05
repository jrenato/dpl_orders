"""
Custom template tags
"""
from django import template

register = template.Library()


@register.filter(name="format_cnpj")
def format_cnpj(cnpj):
    """
    A filter to format a CNPJ (Brazilian company ID) number.
    
    Parameters:
    cnpj (str): The CNPJ to be formatted.
    
    Returns:
    str: The formatted CNPJ.
    """
    cnpj = str(cnpj)

    if len(cnpj) > 18:
        raise ValueError("Invalid CNPJ length")

    # It's already formatted, just return it
    if len(cnpj) == 18:
        return cnpj

    # If not formatted, add leading zeroes and format
    if len(cnpj) < 14:
        cnpj = cnpj.zfill(14)

    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"


@register.filter(name="format_cpf")
def format_cpf(cpf):
    """
    A filter to format a CPF (Brazilian personal ID) number.
    
    Parameters:
    cpf (str): The CPF to be formatted.
    
    Returns:
    str: The formatted CPF.
    """
    cpf = str(cpf)

    if len(cpf) > 14:
        raise ValueError("Invalid CPF length")

    # It's already formatted, just return it
    if len(cpf) == 14:
        return cpf

    # If not formatted, add leading zeroes and format
    if len(cpf) < 11:
        cpf = cpf.zfill(11)

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
