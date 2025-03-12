"""Escriba su código debajo de esta línea."""


def list_reader(tamaño):
    if not isinstance(tamaño, int):
        raise TypeError("Invalid type for list length")
    if tamaño <= 0:
        raise ValueError("List length must be a positive number")
    r_lista = []
    while len(r_lista) < tamaño:
        calculo = len(r_lista) + 1
        u_inp = input(f"Introduce el número {calculo} de {tamaño}: ")
        try:
            number = int(u_inp)
            r_lista.append(number)
        except ValueError:
            print("Por favor, introduce un número válido.")
    return r_lista


if __name__ == "__main__":
    print(list_reader(5))
