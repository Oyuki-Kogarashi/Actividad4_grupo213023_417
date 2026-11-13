# Excepciones personalizadas de Software FJ.
# Todas heredan de ErrorSoftwareFJ, asi se pueden capturar todas juntas.


class ErrorSoftwareFJ(Exception):
    """Excepcion base del sistema."""


class ClienteInvalidoError(ErrorSoftwareFJ):
    """Se usa cuando los datos de un cliente no son validos."""
