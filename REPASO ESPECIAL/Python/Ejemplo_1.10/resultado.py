# (Suponiendo clases base Destination, Node, TripPlannerBase)

class TripPlanner(TripPlannerBase):
    # 1. ATRIBUTO DE CLASE: Contador global de días viajados.
    _all_traveled_days = 0

    def __init__(self):
        super().__init__()
        # 2. ATRIBUTO DE INSTANCIA: Contador de días para este viaje.
        self._days_traveled_instance = 0

    def visit_destination(self, index):
        # 3. MÉTODO PARA VISITAR: Elimina un destino y actualiza contadores.
        destination = self.remove_and_get_item(index) # Asumiendo método auxiliar.
        
        if destination:
            self._days_traveled_instance += destination.days_to_stay
            TripPlanner._all_traveled_days += destination.days_to_stay
        return destination

    @property
    def total_trip_duration(self):
        # 4. PROPIEDAD: Calcula la duración total de los destinos restantes.
        total = 0
        curr = self.first
        while curr:
            total += curr.value.days_to_stay
            curr = curr.next
        return total

    @property
    def days_traveled(self):
        # 5. PROPIEDAD GETTER: Devuelve el contador de la instancia.
        return self._days_traveled_instance

    @days_traveled.setter
    def days_traveled(self, value):
        # 6. PROPIEDAD SETTER: Permite resetear el contador de la instancia a 0.
        if value == 0:
            self._days_traveled_instance = 0

    @classmethod
    def get_all_traveled_days(cls):
        # 7. MÉTODO DE CLASE: Devuelve el contador global.
        return cls._all_traveled_days