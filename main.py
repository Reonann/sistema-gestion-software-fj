from cliente import Cliente
from servicios import ReservaSalas, AlquilerEquipos, AsesoriasEspecializadas
from reserva import Reserva
from excepciones_fj import SoftwareFJException

def ejecutar_sistema():
    print("==================================================")
    print("   SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ      ")
    print("   Fase 4 - Programación Orientada a Objetos      ")
    print("==================================================\n")

    # 1. Simulación de Registro de Clientes con validaciones
    print("--- 1. PRUEBA DE REGISTRO DE CLIENTES ---")
    try:
        cliente1 = Cliente("1020304050", "carlos alberto pérez", "carlos.perez@email.com", "3104567890")
        print(f"Cliente registrado con éxito: {cliente1}")
    except ValueError as e:
        print(f"Error de validación en cliente: {e}")

    try:
        # Prueba de cliente con datos erróneos para verificar excepciones
        cliente_malo = Cliente("123", "Ana", "correo-invalido", "123")
    except ValueError as e:
        print(f"Excepción controlada capturada exitosamente en cliente: {e}")
    
    print("\n--------------------------------------------------\n")

    # 2. Creación de Servicios (Polimorfismo con clases abstractas y especializadas)
    print("--- 2. CREACIÓN DE SERVICIOS ESPECIALIZADOS ---")
    sala_vip = ReservaSalas("SR-01", "Sala de Juntas Ejecutiva", 50000, 15, True)
    equipo_laptop = ReservaSalas("EQ-02", "Laptop Gamer RTX", 35000, 1, False) # Usando simulación de equipo
    asesoria_dev = AsesoriasEspecializadas("AS-03", "Arquitectura de Software", 80000, "Desarrollo Python Avanzado")

    print(sala_vip.obtener_descripcion())
    print(asesoria_dev.obtener_descripcion())

    print("\n--------------------------------------------------\n")

    # 3. Creación de Reservas y Cálculo de Costos
    print("--- 3. GESTIÓN DE RESERVAS Y COSTOS ---")
    try:
        # Reservando la sala por 4 horas con un 10% de descuento
        reserva_sala = Reserva(cliente1, sala_vip, detalle_parametro=4, extra_parametro=10.0)
        print(reserva_sala.obtener_detalle_reserva())
        print("\n")
        
        # Contratando 2 sesiones de asesoría con nivel senior (aplica multiplicador)
        reserva_asesoria = Reserva(cliente1, asesorias_dev, detalle_parametro=2, extra_parametro=True)
        print(reserva_asesoria.obtener_detalle_reserva())

    except SoftwareFJException as ex:
        print(f"Error controlado del Sistema FJ: {ex}")
    except Exception as ex:
        print(f"Error inesperado: {ex}")

    print("\n==================================================")
    print("   EJECUCIÓN FINALIZADA EXITOSAMENTE             ")
    print("==================================================")

if __name__ == "__main__":
    ejecutar_sistema()
