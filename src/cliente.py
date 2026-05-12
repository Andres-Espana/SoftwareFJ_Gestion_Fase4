from base_entity import EntidadBase
from exceptions import DatosInvalidosError

class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, correo):
        super().__init__(id_cliente)
        if not nombre or "@" not in correo:
            raise DatosInvalidosError("Nombre vacío o correo electrónico inválido.")
        self.__nombre = nombre  # Privado
        self.__correo = correo  # Privado

    def obtener_detalles(self):
        return f"Cliente: {self.__nombre} | ID: {self._id_entidad}"
