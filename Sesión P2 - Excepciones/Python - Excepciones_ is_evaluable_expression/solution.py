"""Module with the answer to the problem."""


def is_evaluable_expression(expression: str) -> bool:
    """Return True if the expression is evaluable."""
    components = expression.split()
    if len(components) % 2 == 0:
        raise BadExpression("La expresión debe tener nº impar de componentes.")
    op_valid = {'+', '-', '*', '/'}
    for i in range(len(components)):
        if i % 2 == 0:
            try:
                int(components[i])
            except ValueError:
                raise BadExpression("Operando no entero")
        else:
            if components[i] not in op_valid:
                raise BadExpression("Operador erróneo")
    return True
# NO MODIFIQUE EL CODIGO DEBAJO DE ESTA LINEA


class BadExpression(Exception):
    """Exception for BadExpression."""

    pass
