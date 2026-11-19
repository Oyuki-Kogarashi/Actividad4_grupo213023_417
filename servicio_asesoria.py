
from servicio import Servicio
from excepciones import ServicioInvalidoError
from Validadores import validar_texto


class ServicioAsesoria(Servicio):
    """
    Representa los servicios de asesoria especializada
    ofrecidos por Software FJ.
    """

    def __init__(
        self,
        nombre,
        tarifa_base,
        especialista,
        especialidad,
        disponible=True
    ):
        self.especialista = especialista
        self.especialidad = especialidad

        super().__init__(
            nombre,
            tarifa_base,
            disponible
        )

    @property
    def especialista(self):
        return self.__especialista

    @especialista.setter
    def especialista(self, valor):
        self.__especialista = validar_texto(
            valor,
            campo="Nombre del especialista",
            minimo=3,
            error=ServicioInvalidoError
        )

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        self.__especialidad = validar_texto(
            valor,
            campo="Especialidad",
            minimo=3,
            error=ServicioInvalidoError
        )

    def validar_parametros(self):
        if not self.especialista or not self.especialidad:
            raise ServicioInvalidoError(
                "Debe indicar el especialista y la especialidad."
            )

    def describir_servicio(self):
        return (
            f"Asesoria en {self.especialidad} "
            f"con el especialista {self.especialista}"
        )

    def obtener_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Especialista: {self.especialista} | "
            f"Especialidad: {self.especialidad} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f} | "
            f"Disponible: "
            f"{'Si' if self.disponible else 'No'}"
        )
