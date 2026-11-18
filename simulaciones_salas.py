
from servicio_sala import ServicioSala
from excepciones import ErrorSoftwareFJ
from logger_fj import registrar_evento, registrar_error


def ejecutar():
    print("\n--- SIMULACIONES DE SERVICIOS DE SALAS ---")

    # SIMULACION 1: Registro de sala valida
    try:
        sala1 = ServicioSala(
            "Sala de reuniones",
            50000,
            12
        )

        print("\n1. Sala registrada correctamente")
        print(sala1.obtener_informacion())

        registrar_evento(
            f"Sala registrada: {sala1.nombre}"
        )

    except ErrorSoftwareFJ as error:
        print("Error al registrar la sala:", error)
        registrar_error(
            f"Error al registrar sala: {error}"
        )

    # SIMULACION 2: Capacidad invalida
    try:
        sala2 = ServicioSala(
            "Sala de capacitacion",
            60000,
            0
        )

        print("\n2. Sala registrada:", sala2.nombre)

    except ErrorSoftwareFJ as error:
        print("\n2. Capacidad invalida detectada:", error)
        registrar_error(
            f"Error en capacidad de sala: {error}"
        )

    # SIMULACION 3: Calculo del costo
    try:
        costo = sala1.calcular_costo(
            duracion=3,
            descuento=10,
            impuesto=19
        )

        print("\n3. Calculo del alquiler realizado")
        print(f"Duracion: 3 horas")
        print(f"Tarifa por hora: $50.000")
        print(f"Descuento: 10%")
        print(f"Impuesto: 19%")
        print(f"Costo total: ${costo:,.2f}")

        registrar_evento(
            f"Costo de alquiler calculado: ${costo:,.2f}"
        )

    except ErrorSoftwareFJ as error:
        print("Error en el calculo:", error)
        registrar_error(
            f"Error al calcular alquiler: {error}"
        )

    # SIMULACION 4: Servicio no disponible
    try:
        sala1.desactivar()

        print("\n4. Se intenta utilizar una sala desactivada")

        costo = sala1.calcular_costo(2)

        print(f"Costo del alquiler: ${costo:,.2f}")

    except ErrorSoftwareFJ as error:
        print("Operacion no permitida:", error)
        registrar_error(
            f"Intento de utilizar sala no disponible: {error}"
        )


if __name__ == "__main__":
    ejecutar()
