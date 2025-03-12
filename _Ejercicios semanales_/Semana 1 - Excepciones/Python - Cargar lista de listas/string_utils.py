# Escriba aquí su código
def load_list(fichero):
    try:
        with open(fichero, 'r') as file:
            result = []
            for line in file:
                numbers = list(map(int, line.split()))
                result.append(numbers)
            return result
    except Exception:
        return []
