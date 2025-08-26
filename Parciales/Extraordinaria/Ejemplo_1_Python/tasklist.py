from tasks import *
# esciba aquí la clase TaskList
class TaskList(TaskListBase):
    # Variable de clase para acumular el tiempo total de todas las listas
    _total_time_spent = 0

    def __init__(self):
        super().__init__()
        self._time_spent = 0  # tiempo dedicado a tareas completadas en ESTA lista

    def task_completed(self, index):
        """
        Elimina la tarea en la posición dada, suma su tiempo al acumulado de la lista y del total.
        Devuelve la tarea completada o None si el índice es inválido.
        """
        if index < 0 or index >= self.size:  # asumiendo que TaskListBase mantiene self.size
            return None

        # Recorrer la lista enlazada hasta encontrar la tarea
        prev = None
        current = self.head
        pos = 0
        while current is not None and pos < index:
            prev = current
            current = current.next
            pos += 1

        if current is None:
            return None  # índice fuera de rango

        # Eliminar nodo de la lista enlazada
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

        self.size -= 1  # actualizar tamaño

        # Actualizar tiempos
        self._time_spent += current.data.time  # asumimos que Task tiene atributo .time (en minutos)
        TaskList._total_time_spent += current.data.time

        return current.data

    @property
    def time_left(self):
        """
        Tiempo total en minutos necesario para realizar las tareas pendientes.
        """
        total = 0
        current = self.head
        while current is not None:
            total += current.data.time
            current = current.next
        return total

    @property
    def time_spent(self):
        """Tiempo en minutos dedicado a tareas completadas en esta lista."""
        return self._time_spent

    @time_spent.setter
    def time_spent(self, value):
        """
        Solo permite asignar 0 para resetear el tiempo dedicado en esta lista.
        No hace nada si se intenta asignar otro valor.
        """
        if value == 0:
            # Restar del total global el tiempo que se está reseteando
            TaskList._total_time_spent -= self._time_spent
            self._time_spent = 0

    @classmethod
    def get_total_time_spent(cls):
        """Tiempo total en minutos dedicado a tareas completadas de todas las listas."""
        return cls._total_time_spent

    def get_task_list(self):
        """
        Devuelve una lista de los objetos Task en la lista enlazada, en el mismo orden.
        """
        tasks = []
        current = self.head
        while current is not None:
            tasks.append(current.data)
            current = current.next
        return tasks
