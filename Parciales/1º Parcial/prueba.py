from cuentabancaria import CuentaBancaria
# Ejemplo de uso
cuenta1 = CuentaBancaria('José Rodríguez')
cuenta1.depositar(12)
print(cuenta1)  # CB-001 - Titular: José Rodríguez, Saldo: 12
# Intento de deposito negativo
try:
    cuenta1.depositar(-1)
except ValueError as e:
    print(f"{e.__class__.__name__}: {e}")

# Intento de retirada superior al saldo
try:
    cuenta1.retirar(100)
except ValueError as e:
    print(f"{e.__class__.__name__}: {e}")

cuenta2 = CuentaBancaria('Juan García')
cuenta2.depositar(33)
print(cuenta2)  # CB-002 - Titular: Juan García, Saldo: 33

cuenta3 = CuentaBancaria('José Rodríguez')
cuenta3.depositar(50)
print(cuenta3)  # CB-003 - Titular: José Rodríguez, Saldo: 50

# Prueba de métodos de clase
print("Cuentas abiertas", CuentaBancaria.obtener_total_cuentas())  # 3
print("Total saldo José Rodríguez",
      CuentaBancaria.total_saldo_titular('José Rodríguez'))  # 62
