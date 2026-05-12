from abc import ABC, abstractmethod

class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Encapsulamiento protegido

    @abstractmethod
    def obtener_detalles(self):
        pass
