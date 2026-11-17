from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad
    general dentro del sistema Software FJ.
    """

    @property
    @abstractmethod
    def tipo_entidad(self):
        """Retorna el tipo de entidad."""
        pass

    @abstractmethod
    def obtener_informacion(self):
        """Retorna la informacion de la entidad."""
        pass
