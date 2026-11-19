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

    def __init__(self, cliente, servicio, duracion):
        # Validamos que no falten datos (parametros faltantes)
        if cliente is None:
            raise ReservaInvalidaError("La reserva necesita un cliente.")
        if servicio is None:
            raise ReservaInvalidaError("La reserva necesita un servicio.")
        # La duracion debe ser un numero mayor que cero (bool no cuenta como numero)
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaInvalidaError(f"Duracion invalida: {duracion!r}")

        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = self.PENDIENTE  # toda reserva empieza pendiente
        self._costo = None             # se calcula al procesar

    # Propiedades de solo lectura (encapsulacion)
    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    @property
    def tipo_entidad(self):
        return "Reserva"

    def confirmar(self):
        """Confirma la reserva si esta pendiente y el servicio esta disponible."""
        if self._estado != self.PENDIENTE:
            raise OperacionNoPermitidaError(
                f"No se puede confirmar una reserva {self._estado}."
            )
        if not self._servicio.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio '{self._servicio.nombre}' no esta disponible."
            )
        self._estado = self.CONFIRMADA
        registrar_evento(f"Reserva de {self._cliente.nombre} confirmada.")

    def cancelar(self):
        """Cancela la reserva. No se puede cancelar dos veces."""
        if self._estado == self.CANCELADA:
            raise OperacionNoPermitidaError("La reserva ya estaba cancelada.")
        self._estado = self.CANCELADA
        registrar_evento(f"Reserva de {self._cliente.nombre} cancelada.")

    def procesar(self, descuento=0, impuesto=0):
        """Calcula el costo y confirma la reserva.
        Usa try/except/else/finally y encadenamiento con 'raise ... from'."""
        try:
            # 1. Calcular el costo (puede fallar si el servicio no sirve)
            costo = self._servicio.calcular_costo(self._duracion, descuento, impuesto)
            # 2. Confirmar la reserva (puede fallar por estado o disponibilidad)
            self.confirmar()
        except ErrorSoftwareFJ as error:
            # Se registra el error y se lanza uno nuevo que guarda la causa original
            registrar_error(f"No se pudo procesar la reserva: {error}")
            raise ReservaInvalidaError(
                f"Reserva de {self._cliente.nombre} no procesada"
            ) from error
        else:
            # Solo se ejecuta si NO hubo errores
            self._costo = costo
            registrar_evento(f"Reserva procesada. Costo total: ${costo:,.2f}")
            return costo
        finally:
            # Se ejecuta siempre, haya o no error
            registrar_evento(f"Fin del procesamiento. Estado: {self._estado}")

    def obtener_informacion(self):
        costo = f"${self._costo:,.2f}" if self._costo is not None else "sin calcular"
        return (
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duracion: {self._duracion} h | "
            f"Estado: {self._estado} | Costo: {costo}"
        )

    def __str__(self):
        return self.obtener_informacion()
