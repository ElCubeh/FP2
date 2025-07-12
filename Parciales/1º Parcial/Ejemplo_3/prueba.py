# PROBANDO la clase TarjetaTransporte:
from transporte import TarjetaTransporte

# Crear varias tarjetas para distintos titulares
t1 = TarjetaTransporte("Ana López")
t2 = TarjetaTransporte("Carlos Ruiz")
t3 = TarjetaTransporte("Ana López")

# Mostrar información básica de cada tarjeta
print(t1)
print(t2)
print(t3)

# Recargar una tarjeta y realizar viajes
t1.recargar(20)
t1.viajar(2.5)
t1.viajar(3.0)
print(f"Después de viajar dos veces: {t1}")

# Intentar hacer un viaje sin saldo suficiente
try:
    t2.viajar(5.0)
except ValueError as e:
    print(f"Error al viajar sin saldo: {e}")

# Recargar y viajar correctamente
t2.recargar(10)
t2.viajar(2.5)
print(f"Después de recarga y viaje: {t2}")

# Consultar cuántas tarjetas se han emitido
print(f"Total de tarjetas emitidas: {TarjetaTransporte.total_tarjetas_emitidas()}")
t3.recargar(2.5)
t3.viajar(2.5)

# Consultar viajes total por titular
viajes_ana = TarjetaTransporte.viajes_titular("Ana López")
viajes_carlos = TarjetaTransporte.viajes_titular("Carlos Ruiz")
viajes_ines = TarjetaTransporte.viajes_titular("Inés Morales")  # titular inexistente

print(f"Total viajes Ana López: {saldo_ana}")
print(f"Total viajes Carlos Ruiz: {saldo_carlos}")
print(f"Total viajes Inés Morales: {saldo_ines}")

