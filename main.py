import logging
from cliente import Cliente
from servicio import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from reserva import Reserva
from exceptions import SoftwareFJException

# Configuración de Logs
logging.basicConfig(filename='logs.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def ejecutar_sistema():
    print("--- Sistema Software FJ Iniciado ---")
    
    # Definición de servicios disponibles
    servicios = {
        "sala": ReservaSalas("S01", "Sala de Juntas", 50000),
        "equipo": AlquilerEquipos("E01", "Proyector 4K", 20000),
        "asesoria": AsesoriaEspecializada("A01", "Asesoría Técnica", 80000)
    }
    
    operaciones = [
        # 5 Casos Exitosos (Variando servicios y horas)
        {"id": 1, "nombre": "Juan", "correo": "juan@mail.com", "horas": 3, "tipo": "sala"},
        {"id": 2, "nombre": "Maria", "correo": "m@mail.com", "horas": 2, "tipo": "equipo"}, # +15k mantenimiento
        {"id": 3, "nombre": "Carlos", "correo": "c@mail.com", "horas": 6, "tipo": "asesoria"}, # Descuento 10%
        {"id": 4, "nombre": "Lucia", "correo": "l@mail.com", "horas": 1, "tipo": "sala"},
        {"id": 5, "nombre": "Roberto", "correo": "r@mail.com", "horas": 4, "tipo": "equipo"},
        
        # 5 Casos de Error (Para probar la robustez y los logs)
        {"id": 6, "nombre": "", "correo": "e@mail.com", "horas": 2, "tipo": "sala"},        # Nombre vacío
        {"id": 7, "nombre": "Ana", "correo": "correo_mal", "horas": 2, "tipo": "equipo"},   # Correo sin @
        {"id": 8, "nombre": "Pedro", "correo": "p@mail.com", "horas": -5, "tipo": "sala"},  # Horas negativas
        {"id": 9, "nombre": "Sofia", "correo": "s@mail.com", "horas": 0, "tipo": "equipo"}, # Horas en cero
        {"id": 10, "nombre": "Luis", "correo": "l@mail.com", "horas": 3, "tipo": "desconocido"} # Servicio inexistente
    ]

    for op in operaciones:
        try:
            # Validación de existencia de servicio
            if op["tipo"] not in servicios:
                raise SoftwareFJException(f"El servicio '{op['tipo']}' no existe.")

            # Instanciación dinámica
            c = Cliente(op["id"], op["nombre"], op["correo"])
            s = servicios[op["tipo"]]
            r = Reserva(f"R{op['id']}", c, s, op["horas"])
            
            resultado = r.procesar_reserva()
            print(f"[EXITO] {resultado}")
            logging.info(f"Operación Exitosa: ID {op['id']} - {op['tipo']}")

        except SoftwareFJException as e:
            print(f"[ERROR CONTROLADO] ID {op['id']}: {e}")
            logging.error(f"Error en Operación ID {op['id']}: {e}")
        except Exception as e:
            print(f"[ERROR CRÍTICO]: {e}")
            logging.critical(f"Error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_sistema()
