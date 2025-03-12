"""Ejemplo de uso de la funciones requerida."""

from solution import BadExpression
from solution import is_evaluable_expression
tests = [
            "3",
            "1 + 51 - 8",
            "1 + 51 & 8 / 9999",
            "1 + 51 - 8 * -1.5 / 9999",
            "1 + 51 - 8 * a / 9999"
        ]

for exp in tests:
    try:
        print(is_evaluable_expression(exp))
    except BadExpression as err:
        print(f'{err} en expresión "{exp}"')

# Resultado esperado (se ha añadido entre corchetes el elemento erróneo):
# True
# True
# Operador erróneo ['&'] en expresión "1 + 51 & 8 * -1 / 9999"
# Operando no entero ['-1.5'] en expresión "1 + 51 - 8 * -1.5 / 9999"
# Operando no entero ['a'] en expresión "1 + 51 - 8 * a / 999"
