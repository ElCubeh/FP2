# Escriba aquí su código
from exceptions import FileReadError, FileWriteError, ProcessError
from functions import inspect_file


def control(file_to_inspect: str, file_to_create: str):
    try:
        inspect_file(file_to_inspect, file_to_create)
        return True
    except FileReadError as e:
        return f"Se ha producido la excepción FileReadError con el mensaje: '{str(e)}'"
    except FileWriteError:
        raise ProcessError("Error de proceso")
