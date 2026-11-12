import logging
import os

# Configuración básica del sistema de logs para registrar errores y eventos
log_file = "software_fj_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class SoftwareFJException(Exception):
    """Excepción base para todos los errores controlados del sistema Software FJ."""
    def __init__(self, message):
        super().__init__(message)
        logging.error(f"SoftwareFJException registrada: {message}")


class ClienteNoEncontradoException(SoftwareFJException):
    """Excepción lanzada cuando se busca un cliente que no está registrado."""
    pass


class ServicioNoDisponibleException(SoftwareFJException):
    """Excepción lanzada cuando se intenta contratar un servicio inactivo o inválido."""
    pass


class ReservaInvalidaException(SoftwareFJException):
    """Excepción lanzada cuando los parámetros de la reserva no cumplen las reglas."""
    pass
