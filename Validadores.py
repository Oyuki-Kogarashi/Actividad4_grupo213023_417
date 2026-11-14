# Funciones de validacion reutilizables.
# Cada una lanza una excepcion si el dato es invalido.
# El parametro "error" permite elegir que excepcion lanzar
# (por ejemplo ClienteInvalidoError o ServicioInvalidoError).
import re

from excepciones import ErrorSoftwareFJ


def validar_texto(valor, campo="texto", minimo=3, error=ErrorSoftwareFJ):
    """Verifica que sea un texto con un minimo de caracteres."""
    if not isinstance(valor, str) or len(valor.strip()) < minimo:
        raise error(f"{campo} invalido: debe tener al menos {minimo} caracteres.")
    return valor.strip()
