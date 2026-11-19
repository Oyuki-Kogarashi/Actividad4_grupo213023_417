
from servicio import Servicio
from excepciones import ServicioInvalidoError
from Validadores import validar_texto


class ServicioEquipo(Servicio):
    """
    Representa el alquiler de equipos tecnologicos
    ofrecidos por Software FJ.
    """

    def __init__(
        self,
        nombre,
        tarifa_base,
        tipo_equipo,
        disponible=True
    ):
        self.tipo_equipo = tipo_equipo

        super().__init__(
            nombre,
            tarifa_base,
            disponible
        )

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, valor):
        self.__tipo_equipo = validar_texto(
            valor,
            campo="Tipo de equipo",
            minimo=3,
            error=ServicioInvalidoError
        )

    def validar_parametros(self):
        if not self.tipo_equipo:
            raise ServicioInvalidoError(
                "Debe especificar el tipo de equipo."
            )

    def describir_servicio(self):
        return (
            f"Alquiler de equipo tecnologico: "
            f"{self.tipo_equipo}"
        )

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Equipo: {self.tipo_equipo} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f} | "
            f"Disponible: "
            f"{'Si' if self.disponible else 'No'}"
        )
