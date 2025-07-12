from containerbase import ContainerBase 

class Task:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name}: {self.duration} min"


class TaskList(BaseContainer):
    class Nodo:
        __slots__ = ['task', 'next']
        def __init__(self, task, next=None):
            self.task = task
            self.next = next

    def __init__(self):
        super().__init__()
        self._head = None     # Primer nodo de la lista
        self._tail = None     # Último nodo de la lista
        self._count = 0       # Contador de tareas pendientes
        self._time_spent = 0  # Tiempo total dedicado a tareas completadas

    def add_task(self, task):
        """Añade una nueva tarea al final de la lista"""
        new_node = TaskList.Nodo(task)
        if self._head is None:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._count += 1

    def get_task(self, index):
        """Devuelve la tarea en la posición indicada (None si no existe)"""
        if index < 0 or index >= self._count:
            return None
        current = self._head
        for _ in range(index):
            current = current.next
        return current.task

    def task_completed(self, index):
        """Elimina y devuelve la tarea completada en la posición indicada"""
        if index < 0 or index >= self._count:
            return None

        # Caso especial: eliminar el primer nodo
        if index == 0:
            removed_task = self._head.task
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self._count -= 1
            self._time_spent += removed_task.duration
            return removed_task

        # Buscar el nodo anterior al que se eliminará
        prev = self._head
        for _ in range(index - 1):
            prev = prev.next
        
        removed_node = prev.next
        removed_task = removed_node.task
        prev.next = removed_node.next
        
        # Actualizar tail si se eliminó el último nodo
        if removed_node.next is None:
            self._tail = prev
        
        self._count -= 1
        self._time_spent += removed_task.duration
        return removed_task

    @property
    def time_left(self):
        """Tiempo total pendiente de todas las tareas"""
        total = 0
        current = self._head
        while current is not None:
            total += current.task.duration
            current = current.next
        return total

    @property
    def time_spent(self):
        """Tiempo total dedicado a tareas completadas"""
        return self._time_spent

    def __str__(self):
        """Representación de cadena de la lista de tareas"""
        if self._head is None:
            return "None"
        
        parts = []
        current = self._head
        while current is not None:
            parts.append(f"[{current.task}]")
            current = current.next
        return "->".join(parts) + "->None"