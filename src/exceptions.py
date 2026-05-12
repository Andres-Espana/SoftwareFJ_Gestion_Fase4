class SoftwareFJException(Exception):
    """Clase base para excepciones del sistema."""
    pass

class DatosInvalidosError(SoftwareFJException):
    """Se lanza cuando los datos de entrada no son válidos."""
    pass

class ReservaIncorrectaError(SoftwareFJException):
    """Se lanza cuando una reserva no puede procesarse."""
    pass

class ServicioNoDisponibleError(SoftwareFJException):
    """Se lanza cuando el servicio solicitado no está en catálogo."""
    pass
