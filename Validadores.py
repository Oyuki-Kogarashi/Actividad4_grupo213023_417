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


def validar_email(valor, error=ErrorSoftwareFJ):
    """Verifica que el correo tenga un formato valido (ej: ana@mail.com)."""
    patron = r"[\w.+-]+@[\w-]+\.[\w.-]+"
    if not isinstance(valor, str) or not re.fullmatch(patron, valor):
        raise error(f"Email invalido: {valor!r}")
    return valor


def validar_telefono(valor, error=ErrorSoftwareFJ):
    """Verifica que el telefono tenga solo numeros (7 a 10 digitos)."""
    if not (isinstance(valor, str) and valor.isdigit() and 7 <= len(valor) <= 10):
        raise error(f"Telefono invalido: {valor!r} (debe tener 7 a 10 digitos).")
    return valor


def validar_numero_positivo(valor, campo="numero", error=ErrorSoftwareFJ):
    """Verifica que sea un numero mayor que cero."""
    if isinstance(valor, bool) or not isinstance(valor, (int, float)) or valor <= 0:
        raise error(f"{campo} invalido: {valor!r} (debe ser mayor que 0).")
    return valor
