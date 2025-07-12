# ESCRIBA AQUÍ LA CLASE
class TarjetaTransporte:
    # descomente la siguiente línea si quiere usarla
    # __viajes_titular: dict[str, int] = {}  # titular: número de viajes
class TarjetaTransporte:
    _contador_tarjetas = 1000000
    _total_tarjetas = 0
    _viajes_por_titular = {}

    def __init__(self, titular):
        TarjetaTransporte._contador_tarjetas += 1
        self._numero_tarjeta = f"TT-{TarjetaTransporte._contador_tarjetas}"
        self._titular = titular
        self._saldo = 0.0
        self._viajes_realizados = 0
        TarjetaTransporte._total_tarjetas += 1
        if titular not in TarjetaTransporte._viajes_por_titular:
            TarjetaTransporte._viajes_por_titular[titular] = 0

    @property
    def numero_tarjeta(self):
        return self._numero_tarjeta

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def viajes_realizados(self):
        return self._viajes_realizados

    def recargar(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad a recargar no puede ser negativa")
        self._saldo += cantidad

    def viajar(self, costo_viaje):
        if costo_viaje < 0:
            raise ValueError("El costo del viaje no puede ser negativo")
        if self._saldo < costo_viaje:
            raise ValueError("Saldo insuficiente para realizar el viaje")
        self._saldo -= costo_viaje
        self._viajes_realizados += 1
        TarjetaTransporte._viajes_por_titular[self._titular] += 1

    @classmethod
    def total_tarjetas_emitidas(cls):
        return cls._total_tarjetas

    @classmethod
    def viajes_titular(cls, nombre_titular):
        return cls._viajes_por_titular.get(nombre_titular, 0)

    def __str__(self):
        return f"{self.numero_tarjeta} - Titular: {self.titular}, Saldo: {self.saldo}, Viajes: {self.viajes_realizados}"