"""En este archivo debe escribirse las solución requerida."""


def factorial(n):
    assert isinstance(n, int) and n >= 0, "Invalid data"
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial(5))
