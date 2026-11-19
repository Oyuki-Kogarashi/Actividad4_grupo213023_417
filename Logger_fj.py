# Configuracion del archivo de logs (fj_log.txt).
# Aqui se guardan los eventos y errores del programa.
import logging

NOMBRE_ARCHIVO = "fj_log.txt"

# Creamos el logger con un nombre propio
logger = logging.getLogger("software_fj")
logger.setLevel(logging.INFO)

# Solo agregamos el manejador una vez (evita lineas repetidas en el log)
if not logger.handlers:
    manejador = logging.FileHandler(NOMBRE_ARCHIVO, mode="w", encoding="utf-8")
    formato = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    manejador.setFormatter(formato)
    logger.addHandler(manejador)


def registrar_evento(mensaje):
    """Guarda un evento normal en el log."""
    logger.info(mensaje)


def registrar_error(mensaje):
    """Guarda un error en el log."""
    logger.error(mensaje)
