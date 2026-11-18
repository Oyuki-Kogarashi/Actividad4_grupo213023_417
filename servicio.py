
from abc import ABC, abstractmethod
import math

from entidad import Entidad
from excepciones import (
    ServicioInvalidoError,
    ServicioNoDisponibleError,
    CalculoInconsistenteError
)
from Validadores import validar_texto, validar_numero_positivo


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa los servicios ofrecidos
    por la empresa Software FJ.
    """

    def __init__(self, nombre, tarifa_base, disponible=True):
        self.nombre = nombre
        self.tarifa_base = tarifa_base
        self.disponible = disponible

        # Cada servicio especializado valida sus propios datos.
        self.validar_parametros()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = validar_texto(
            valor,
            campo="Nombre del servicio",
            minimo=3,
            error=ServicioInvalidoError
        )

    @property
    def tarifa_base(self):
        return self.__tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, (int, float))
            or not math.isfinite(valor)
        ):
            raise ServicioInvalidoError(
                "La tarifa debe ser un numero valido."
            )

        self.__tarifa_base = validar_numero_positivo(
            valor,
            campo="Tarifa base",
            error=ServicioInvalidoError
        )

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, valor):
        if not isinstance(valor, bool):
            raise ServicioInvalidoError(
                "La disponibilidad debe ser True o False."
            )
        self.__disponible = valor

    @property
    def tipo_entidad(self):
        return "Servicio"

    @abstractmethod
    def validar_parametros(self):
        """Valida los datos particulares de cada servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Describe las características del servicio."""
        pass

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """
        Calcula el costo del servicio.
        Permite utilizar duración, descuento e impuesto opcionales.
        """

        if not self.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio '{self.nombre}' no esta disponible."
            )

        valores = (duracion, descuento, impuesto)

        for valor in valores:
            if (
                isinstance(valor, bool)
                or not isinstance(valor, (int, float))
                or not math.isfinite(valor)
            ):
                raise ServicioInvalidoError(
                    "Los valores del calculo deben ser numericos."
                )

        if duracion <= 0:
            raise ServicioInvalidoError(
                "La duracion debe ser mayor que cero."
            )

        if not 0 <= descuento <= 100:
            raise ServicioInvalidoError(
                "El descuento debe estar entre 0 y 100."
            )

        if not 0 <= impuesto <= 100:
            raise ServicioInvalidoError(
                "El impuesto debe estar entre 0 y 100."
            )

        subtotal = self.tarifa_base * duracion
        valor_descuento = subtotal * descuento / 100
        subtotal_con_descuento = subtotal - valor_descuento
        total = subtotal_con_descuento * (1 + impuesto / 100)

        if not math.isfinite(total) or total < 0:
            raise CalculoInconsistenteError(
                "No fue posible calcular un costo valido."
            )

        return round(total, 2)

    def obtener_informacion(self):
        return (
            f"Tipo: {self.tipo_entidad} | "
            f"Servicio: {self.nombre} | "
            f"Tarifa base: ${self.tarifa_base:,.2f} | "
            f"Disponible: {'Si' if self.disponible else 'No'} | "
            f"{self.describir_servicio()}"
        )

    def activar(self):
        self.disponible = True

    def desactivar(self):
        self.disponible = False

    def __str__(self):
        return self.obtener_informacion()
