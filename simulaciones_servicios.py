
from servicio_equipo import ServicioEquipo
from servicio_asesoria import ServicioAsesoria
from excepciones import ErrorSoftwareFJ
from logger_fj import registrar_evento, registrar_error


def ejecutar():
    print("\n--- SIMULACIONES DE SERVICIOS ---")

    # SIMULACION 1: Registro de equipo valido
    try:
        equipo1 = ServicioEquipo(
            "Alquiler de computador",
            25000,
            "Computador portatil"
        )

        print("\n1. Equipo registrado correctamente")
        print(equipo1.obtener_informacion())

        registrar_evento(
            f"Equipo registrado: {equipo1.nombre}"
        )

    except ErrorSoftwareFJ as error:
        print("Error al registrar equipo:", error)
        registrar_error(
            f"Error al registrar equipo: {error}"
        )

    # SIMULACION 2: Tipo de equipo invalido
    try:
        equipo2 = ServicioEquipo(
            "Alquiler de equipo",
            30000,
            ""
        )

        print(equipo2.obtener_informacion())

    except ErrorSoftwareFJ as error:
        print("\n2. Tipo de equipo invalido detectado:", error)
        registrar_error(
            f"Error en tipo de equipo: {error}"
        )

    # SIMULACION 3: Registro de asesoria valida
    try:
        asesoria1 = ServicioAsesoria(
            "Asesoria informatica",
            80000,
            "Carlos Ramirez",
            "Sistemas informaticos"
        )

        print("\n3. Asesoria registrada correctamente")
        print(asesoria1.obtener_informacion())

        registrar_evento(
            f"Asesoria registrada: {asesoria1.nombre}"
        )

    except ErrorSoftwareFJ as error:
        print("Error al registrar asesoria:", error)
        registrar_error(
            f"Error al registrar asesoria: {error}"
        )

    # SIMULACION 4: Especialista invalido
    try:
        asesoria2 = ServicioAsesoria(
            "Asesoria tecnica",
            70000,
            "",
            "Soporte tecnico"
        )

        print(asesoria2.obtener_informacion())

    except ErrorSoftwareFJ as error:
        print("\n4. Especialista invalido detectado:", error)
        registrar_error(
            f"Error en especialista: {error}"
        )

    # SIMULACION 5: Calculo del alquiler de equipo
    try:
        costo_equipo = equipo1.calcular_costo(
            duracion=4,
            descuento=10
        )

        print("\n5. Calculo del alquiler de equipo")
        print("Duracion: 4 horas")
        print("Tarifa por hora: $25.000")
        print("Descuento: 10%")
        print(f"Costo total: ${costo_equipo:,.2f}")

        registrar_evento(
            f"Costo de equipo calculado: ${costo_equipo:,.2f}"
        )

    except ErrorSoftwareFJ as error:
        print("Error en calculo de equipo:", error)
        registrar_error(
            f"Error en calculo de equipo: {error}"
        )

    # SIMULACION 6: Calculo de asesoria
    try:
        costo_asesoria = asesoria1.calcular_costo(
            duracion=2,
            impuesto=19
        )

        print("\n6. Calculo de asesoria")
        print("Duracion: 2 horas")
        print("Tarifa por hora: $80.000")
        print("Impuesto: 19%")
        print(f"Costo total: ${costo_asesoria:,.2f}")

        registrar_evento(
            f"Costo de asesoria calculado: "
            f"${costo_asesoria:,.2f}"
        )

    except ErrorSoftwareFJ as error:
        print("Error en calculo de asesoria:", error)
        registrar_error(
            f"Error en calculo de asesoria: {error}"
        )

    # SIMULACION 7: Servicio desactivado
    try:
        equipo1.desactivar()

        print("\n7. Intento de utilizar equipo desactivado")

        equipo1.calcular_costo(2)

    except ErrorSoftwareFJ as error:
        print("Operacion no permitida:", error)
        registrar_error(
            f"Intento de utilizar equipo desactivado: {error}"
        )


if __name__ == "__main__":
    ejecutar()
