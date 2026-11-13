# Excepciones personalizadas de Software FJ.
# Todas heredan de ErrorSoftwareFJ, asi se pueden capturar todas juntas.


class ErrorSoftwareFJ(Exception):
    """Excepcion base del sistema."""


class ClienteInvalidoError(ErrorSoftwareFJ):
    """Se usa cuando los datos de un cliente no son validos."""


class ServicioInvalidoError(ErrorSoftwareFJ):
    """Se usa cuando los parametros de un servicio no son validos."""


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se usa cuando se intenta reservar un servicio no disponible."""


class ReservaInvalidaError(ErrorSoftwareFJ):
    """Se usa cuando una reserva no se puede crear o procesar."""


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Se usa cuando una operacion no esta permitida en el estado actual."""


class CalculoInconsistenteError(ErrorSoftwareFJ):
    """Se usa cuando un calculo de costos da un resultado incorrecto."""