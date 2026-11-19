# Clase Reserva: une un cliente, un servicio, una duracion y un estado.
from entidad import Entidad
from excepciones import (
    ErrorSoftwareFJ,
    OperacionNoPermitidaError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
)
from logger_fj import registrar_error, registrar_evento


class Reserva(Entidad):
    """Reserva de un servicio hecha por un cliente."""

    # Estados posibles de la reserva
    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"
