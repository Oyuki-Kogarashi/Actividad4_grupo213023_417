
from servicio import Servicio
from excepciones import ServicioInvalidoError


class ServicioSala(Servicio):
    """
    Representa el servicio de alquiler de salas
    para reuniones de Software FJ.
    """

    def __init__(
        self,
        nombre,
        tarifa_base,
        capacidad,
        disponible=True
    ):
        self.capacidad = capacidad

        super().__init__(
            nombre,
            tarifa_base,
            disponible
        )

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if (
            isinstance(valor, bool)
            or not isinstance(valor, int)
            or valor <= 0
        ):
            raise ServicioInvalidoError(
                "La capacidad de la sala debe ser "
                "un numero entero mayor que cero."
            )

        self.__capacidad = valor

    def validar_parametros(self):
        if self.capacidad <= 0:
            raise ServicioInvalidoError(
                "La capacidad de la sala no es valida."
            )

    def describir_servicio(self):
        return (
            f"Capacidad: {self.capacidad} personas"
        )

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f} | "
            f"Capacidad: {self.capacidad} personas | "
            f"Disponible: {'Si' if self.disponible else 'No'}"
        )
