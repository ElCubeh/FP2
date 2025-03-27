"""Escriba aquí su código."""


def diferencial(lista):
    if len(lista) > 0:
        prev_len = len(lista[0])
        yield prev_len

        for i in range(1, len(lista)):
            curr_len = len(lista[i])
            yield curr_len - prev_len
            prev_len = curr_len


if __name__ == "__main__":
    # Escriba aquí el código que quiera probar
    pass
