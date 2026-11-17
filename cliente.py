from entidad import Entidad

from excepciones import ClienteInvalidoError

from Validadores import (
    validar_texto,
    validar_email,
    validar_telefono
)


class Cliente(Entidad):
    """
    Representa un cliente de Software FJ.
    Contiene datos personales protegidos y validados.
    """

    def __init__(self, nombre, email, telefono):

        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        self.__nombre = validar_texto(
            valor,
            campo="Nombre del cliente",
            minimo=3,
            error=ClienteInvalidoError
        )

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):

        self.__email = validar_email(
            valor,
            error=ClienteInvalidoError
        )

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        self.__telefono = validar_telefono(
            valor,
            error=ClienteInvalidoError
        )

    @property
    def tipo_entidad(self):
        return "Cliente"

    def obtener_informacion(self):

        return (
            f"Nombre: {self.nombre} | "
            f"Email: {self.email} | "
            f"Telefono: {self.telefono}"
        )

    def __str__(self):
        return self.obtener_informacion()