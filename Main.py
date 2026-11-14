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

