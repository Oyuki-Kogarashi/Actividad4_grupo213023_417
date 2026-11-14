# Programa principal de Software FJ.
# Ejecuta las simulaciones de cada integrante y muestra un resumen del log.
# Para correrlo:  python main.py
import importlib

from logger_fj import NOMBRE_ARCHIVO, registrar_error, registrar_evento

# Modulos de simulaciones. Cada uno debe tener una funcion ejecutar().
MODULOS = [
    "simulaciones_clientes",    # Integrante 2
    "simulaciones_salas",       # Integrante 3
    "simulaciones_servicios",   # Integrante 4
    "simulaciones_reservas",    # Integrante 5
]


def correr_simulaciones():
    """Importa y ejecuta cada modulo sin que un error detenga el programa."""
    for nombre in MODULOS:
        print(f"\n=== {nombre} ===")
        try:
            modulo = importlib.import_module(nombre)
            modulo.ejecutar()
        except ModuleNotFoundError as e:
            # Falta un archivo (por ejemplo, un companero aun no lo sube)
            print(f"  Aviso: no se encontro '{e.name}'. Se omite este modulo.")
            registrar_error(f"Modulo no encontrado: {e.name} (en {nombre})")
        except Exception as e:
            # Cualquier otro error: se registra y se continua
            print(f"  Error en {nombre}: {e}")
            registrar_error(f"Error inesperado en {nombre}: {e!r}")
        else:
            registrar_evento(f"Modulo {nombre} ejecutado correctamente")


def mostrar_resumen():
    """Lee el archivo de logs y cuenta eventos y errores."""
    eventos = 0
    errores = 0
    lineas_error = []
    with open(NOMBRE_ARCHIVO, encoding="utf-8") as archivo:
        for linea in archivo:
            if "| INFO |" in linea:
                eventos += 1
            elif "| ERROR |" in linea or "| CRITICAL |" in linea:
                errores += 1
                lineas_error.append(linea.strip())

    print("\n" + "=" * 40)
    print("RESUMEN DEL LOG")
    print("=" * 40)
    print(f"Eventos registrados: {eventos}")
    print(f"Errores registrados: {errores}")
    for linea in lineas_error[-5:]:
        print("  -", linea)
    print(f"\nRevisa el archivo {NOMBRE_ARCHIVO} para ver todo el detalle.")


def main():
    registrar_evento("=== Inicio de la simulacion Software FJ ===")
    correr_simulaciones()
    registrar_evento("=== Fin de la simulacion ===")
    mostrar_resumen()


if __name__ == "__main__":
    main()
