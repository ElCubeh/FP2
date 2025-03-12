"""En este archivo se debe escribir la solución al problema planteado."""
from exceptions import AssocError, CheckError
from functions import assoc


def control(extensiones, programas):
    try:
        resultado = assoc(extensiones, programas)
        if resultado < 5:
            return resultado
        else:
            raise AssocError(f"Error de asociación {resultado}")
    except CheckError as e:
        return f"Se ha producido la excepción CheckError con el mensaje: '{str(e)}'"

