from abc import abstractmethod
from base_entity import EntidadBase

class Servicio(EntidadBase):
    def __init__(self, id_servicio, nombre_servicio, costo_base):
        super().__init__(id_servicio)
        self.nombre = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, horas):
        """Método abstracto para polimorfismo de costos"""
        pass

    # Implementación base para cumplir con la jerarquía de EntidadBase
    def obtener_detalles(self):
        return f"SERVICIO: {self.nombre} (ID: {self._id_entidad})"

class ReservaSalas(Servicio):
    def calcular_costo(self, horas):
        return self.costo_base * horas
    
    def obtener_detalles(self):
        return f"TIPO: Reserva de Sala | Nombre: {self.nombre} | ID: {self._id_entidad}"

class AlquilerEquipos(Servicio):
    def calcular_costo(self, horas):
        # Sobrecarga lógica: costo base + mantenimiento
        return (self.costo_base * horas) + 15000
    
    def obtener_detalles(self):
        return f"TIPO: Alquiler de Equipo | Nombre: {self.nombre} | ID: {self._id_entidad}"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        # Descuento si es más de 5 horas
        total = self.costo_base * horas
        return total * 0.9 if horas > 5 else total

    def obtener_detalles(self):
        return f"TIPO: Asesoría Técnica | Nombre: {self.nombre} | ID: {self._id_entidad}"
