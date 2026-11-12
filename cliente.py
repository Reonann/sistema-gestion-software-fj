import re
from excepciones_fj import ClienteNoEncontradoException

class Cliente:
    """Clase que representa a un cliente de Software FJ con validaciones estrictas y encapsulación."""
    
    def __init__(self, cedula: str, nombre: str, correo: str, telefono: str):
        self.cedula = self._validar_cedula(cedula)
        self.nombre = self._validar_nombre(nombre)
        self.correo = self._validar_correo(correo)
        self.telefono = self._validar_telefono(telefono)

    def _validar_cedula(self, cedula: str) -> str:
        if not cedula or not cedula.isdigit() or len(cedula) < 6:
            raise ValueError("La cédula debe contener solo dígitos y tener al menos 6 caracteres.")
        return cedula

    def _validar_nombre(self, nombre: str) -> str:
        if not nombre or len(nombre.strip()) < 3:
            raise ValueError("El nombre del cliente no puede estar vacío y debe tener al menos 3 caracteres.")
        return nombre.strip().title()

    def _validar_correo(self, correo: str) -> str:
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, correo):
            raise ValueError(f"El correo electrónico '{correo}' no tiene un formato válido.")
        return correo

    def _validar_telefono(self, telefono: str) -> str:
        if not telefono or not telefono.isdigit() or len(telefono) < 7:
            raise ValueError("La teléfono debe contener solo números y al menos 7 dígitos.")
        return telefono

    def __str__(self):
        return f"Cliente [Cédula: {self.cedula}, Nombre: {self.nombre}, Correo: {self.correo}, Teléfono: {self.telefono}]"
