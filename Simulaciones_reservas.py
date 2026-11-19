# Simulaciones 9 a 12: reservas exitosas y fallidas. 
from cliente import Cliente
from excepciones import ErrorSoftwareFJ
from logger_fj import registrar_error, registrar_evento
from reserva import Reserva
from servicio_sala import ServicioSala


def ejecutar():
    print("\n--- SIMULACIONES DE RESERVAS ---")

    # Datos de apoyo: un cliente y una sala validos
    cliente = Cliente("Maria Lopez", "maria@mail.com", "3201234567")
    sala = ServicioSala("Sala Orion", 40000, 10)

    # SIMULACION 9: Reserva exitosa
    try:
        reserva = Reserva(cliente, sala, 3)
        costo = reserva.procesar(descuento=10, impuesto=19)
    except ErrorSoftwareFJ as error:
        print("9. Error inesperado:", error)
        registrar_error(f"Simulacion 9: {error}")
    else:
        print("\n9. Reserva exitosa")
        print(reserva.obtener_informacion())
        registrar_evento(f"Simulacion 9 OK. Costo: ${costo:,.2f}")

    # SIMULACION 10: Servicio no disponible
    try:
        sala.desactivar()  # la sala deja de estar disponible
        reserva2 = Reserva(cliente, sala, 2)
        reserva2.procesar()
    except ErrorSoftwareFJ as error:
        print("\n10. Servicio no disponible detectado:", error)
        # __cause__ guarda el error original (encadenamiento con 'from')
        print("    Causa original:", error.__cause__)
        registrar_error(f"Simulacion 10: {error} | causa: {error.__cause__}")
    finally:
        sala.activar()  # dejamos la sala activa para las demas pruebas

    # SIMULACION 11: Cancelar dos veces la misma reserva
    try:
        reserva3 = Reserva(cliente, sala, 1)
        reserva3.procesar()
        reserva3.cancelar()
        print("\n11. Primera cancelacion realizada. Estado:", reserva3.estado)
        reserva3.cancelar()  # segunda vez: debe fallar
    except ErrorSoftwareFJ as error:
        print("    Segunda cancelacion rechazada:", error)
        registrar_error(f"Simulacion 11: {error}")

    # SIMULACION 12: Reserva sin cliente
    try:
        reserva4 = Reserva(None, sala, 2)
    except ErrorSoftwareFJ as error:
        print("\n12. Reserva sin cliente detectada:", error)
        registrar_error(f"Simulacion 12: {error}")
    else:
        print(reserva4.obtener_informacion())


if __name__ == "__main__":
    ejecutar()
