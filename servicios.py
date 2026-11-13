from abc import ABC, abstractmethod
from excepciones_fj import ServicioNoDisponibleException

class Servicio(ABC):
    """Clase abstracta que representa entidades generales de servicios en Software FJ."""
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, disponible: bool = True):
        self.id_servicio = self._validar_id(id_servicio)
        self.nombre = self._validar_nombre(nombre)
        self.costo_base = self._validar_costo(costo_base)
        self.disponible = disponible

    def _validar_id(self, id_servicio: str) -> str:
        if not id_servicio or len(id_servicio.strip()) < 2:
            raise ValueError("El ID del servicio no puede estar vacío y debe tener al menos 2 caracteres.")
        return id_servicio.strip()

    def _validar_nombre(self, nombre: str) -> str:
        if not nombre or len(nombre.strip()) < 3:
            raise ValueError("El nombre del servicio debe tener al menos 3 caracteres.")
        return nombre.strip().title()

    def _validar_costo(self, costo: float) -> float:
        if costo < 0:
            raise ValueError("El costo base del servicio no puede ser negativo.")
        return float(costo)

    @abstractmethod
    def calcular_costo(self) -> float:
        """Método abstractor para calcular el costo final del servicio."""
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        """Método abstractor para obtener la descripción detallada del servicio."""
        pass


class ReservaSalas(Servicio):
    """Servicio especializado para la reserva de salas en Software FJ."""
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, capacidad: int, proyector: bool = True):
        super().__init__(id_servicio, nombre, costo_base)
        self.capacidad = self._validar_capacidad(capacidad)
        self.proyector = proyector

    def _validar_capacidad(self, capacidad: int) -> int:
        if capacidad <= 0:
            raise ValueError("La capacidad de la sala debe ser mayor a cero.")
        return int(capacidad)

    # Método sobrecargado / con parámetros opcionales para cálculo de costos con impuestos o descuentos
    def calcular_costo(self, horas: int = 1, descuento_porcentaje: float = 0.0) -> float:
        if not self.disponible:
            raise ServicioNoDisponibleException(f"La sala '{self.nombre}' no se encuentra disponible actualmente.")
        if horas <= 0:
            raise ValueError("Las horas de reserva deben ser mayores a cero.")
        
        subtotal = self.costo_base * horas
        descuento = subtotal * (descuento_porcentaje / 100)
        total = subtotal - descuento
        return round(total, 2)

    def obtener_descripcion(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        extra = "Incluye Proyector" if self.proyector else "Sin Proyector"
        return f"Reserva de Sala: {self.nombre} | Capacidad: {self.capacidad} personas | {extra} | Estado: {estado}"


class AlquilerEquipos(Servicio):
    """Servicio especializado para el alquiler de equipos tecnológicos."""
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, marca: str, modelo: str):
        super().__init__(id_servicio, nombre, costo_base)
        self.marca = marca.strip()
        self.modelo = modelo.strip()

    def calcular_costo(self, dias: int = 1, seguro_adicional: bool = False) -> float:
        if not self.disponible:
            raise ServicioNoDisponibleException(f"El equipo '{self.nombre}' no está disponible para alquiler.")
        if dias <= 0:
            raise ValueError("Los días de alquiler deben ser mayores a cero.")
        
        subtotal = self.costo_base * dias
        costo_seguro = 15000 * dias if seguro_adicional else 0.0
        return round(subtotal + costo_seguro, 2)

    def obtener_descripcion(self) -> str:
        return f"Alquiler de Equipo: {self.nombre} ({self.marca} {self.modelo}) | Costo diario: ${self.costo_base}"


class AsesoriasEspecializadas(Servicio):
    """Servicio especializado para asesorías técnicas profesionales."""
    
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, area_especialidad: str):
        super().__init__(id_servicio, nombre, costo_base)
        self.area_especialidad = area_especialidad.strip()

    def calcular_costo(self, sesiones: int = 1, nivel_senior: bool = False) -> float:
        if not self.disponible:
            raise ServicioNoDisponibleException(f"La asesoría en '{self.area_especialidad}' no está disponible.")
        if sesiones <= 0:
            raise ValueError("El número de sesiones debe ser mayor a cero.")
        
        multiplicador = 1.5 if nivel_senior else 1.0
        subtotal = self.costo_base * sesiones * multiplicador
        return round(subtotal, 2)

    def obtener_descripcion(self) -> str:
        return f"Asesoría Especializada: {self.nombre} | Área: {self.area_especialidad} | Tarifa Base: ${self.costo_base}"
