from datetime import datetime
from cliente import Cliente
from servicios import Servicio
from excepciones_fj import ReservaInvalidaException

class Reserva:
    """Clase que gestiona las reservas de servicios para los clientes en Software FJ."""
    
    _contador_id = 1000

    def __init__(self, cliente: Cliente, servicio: Servicio, detalle_parametro: int = 1, extra_parametro: float = 0.0):
        Reserva._contador_id += 1
        self.id_reserva = f"RES-{Reserva._contador_id}"
        self.cliente = cliente
        self.servicio = servicio
        self.detalle_parametro = detalle_parametro
        self.extra_parametro = extra_parametro
        self.fecha_reserva = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.costo_total = self._calcular_costo_total()

    def _calcular_costo_total(self) -> float:
        try:
            # Polimorfismo: Llamamos al método calcular_costo propio de cada servicio especializado
            return self.servicio.calcular_costo(self.detalle_parametro, self.extra_parametro)
        except Exception as e:
            raise ReservaInvalidaException(f"Error al calcular el costo de la reserva: {str(e)}")

    def obtener_detalle_reserva(self) -> str:
        return (
            f"=== RESERVA {self.id_reserva} ===\n"
            f"Fecha de Creación: {self.fecha_reserva}\n"
            f"Datos del Cliente: {self.cliente.nombre} (Cédula: {self.cliente.cedula})\n"
            f"Detalle del Servicio: {self.servicio.obtener_descripcion()}\n"
            f"Parámetro de contratación (Horas/Días/Sesiones): {self.detalle_parametro}\n"
            f"Costo Total: ${self.costo_total:,.2f}\n"
            f"================================"
        )
