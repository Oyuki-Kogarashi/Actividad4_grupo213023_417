from cliente import Cliente

from excepciones import ClienteInvalidoError

from logger_fj import registrar_evento, registrar_error


def ejecutar():

    print("\n--- SIMULACIONES DE CLIENTES ---")

    # SIMULACION 1: Cliente valido

    try:

        cliente1 = Cliente(
            "Samuel Tilano",
            "samuel@gmail.com",
            "3124567890"
        )

    except ClienteInvalidoError as error:

        print("Error al registrar el cliente:", error)
        registrar_error(f"Cliente valido: {error}")

    else:

        print("1. Cliente registrado correctamente")
        print(cliente1.obtener_informacion())

        registrar_evento(
            f"Cliente registrado: {cliente1.nombre}"
        )

    # SIMULACION 2: Email invalido

    try:

        cliente2 = Cliente(
            "Carlos Ramirez",
            "correo_incorrecto",
            "3104567890"
        )

    except ClienteInvalidoError as error:

        print("2. Email invalido detectado:", error)

        registrar_error(
            f"Error en registro de email: {error}"
        )

    else:

        print(cliente2.obtener_informacion())

    # SIMULACION 3: Telefono invalido

    try:

        cliente3 = Cliente(
            "Laura Martinez",
            "laura@gmail.com",
            "123"
        )

    except ClienteInvalidoError as error:

        print("3. Telefono invalido detectado:", error)

        registrar_error(
            f"Error en registro de telefono: {error}"
        )

    else:

        print(cliente3.obtener_informacion())


if __name__ == "__main__":
    ejecutar()