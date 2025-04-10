# ESCRIBA AQUÍ LA CLASE
class CuentaBancaria:
    __titular_suma: dict[str, float] = {}

    def __init__(self, titular: str):
        self._titular = titular
        self._saldo = 0.0
        CuentaBancaria._total_cuentas += 1
        self._codigo_cuenta = f"CB-{CuentaBancaria._total_cuentas:03d}"

        if titular not in CuentaBancaria._cuentas_por_titular:
            CuentaBancaria._cuentas_por_titular[titular] = []
        CuentaBancaria._cuentas_por_titular[titular].append(self)
    
    @property
    def codigo_cuenta(self) -> str:
        return self._codigo_cuenta

    @property
    def titular(self) -> str:
        return self._titular

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad a depositar no puede ser negativa")
        self._saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad a retirar no puede ser negativa")
        if cantidad > self._saldo:
            raise ValueError("Saldo insuficiente para realizar la operación")
        self._saldo -= cantidad

    @classmethod
    def obtener_total_cuentas(cls) -> int:
        return cls._total_cuentas

    @classmethod
    def total_saldo_titular(cls, titular: str) -> float:
        if titular not in cls._cuentas_por_titular:
            return 0.0
        return sum(cuenta.saldo for cuenta in cls._cuentas_por_titular[titular])

    def __str__(self) -> str:
        return f"{self.codigo_cuenta} - Titular: {self.titular}, Saldo: {self.saldo}"
