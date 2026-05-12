from datetime import datetime
from exceptions import ReservaIncorrectaError

class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaIncorrectaError("La duración debe ser mayor a cero.")
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.fecha = datetime.now()

    def procesar_reserva(self):
        costo = self.servicio.calcular_costo(self.duracion)
        return f"Reserva {self.id_reserva} confirmada para {self.cliente.obtener_detalles()}. Total: ${costo}"
