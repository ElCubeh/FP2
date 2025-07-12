from tasks import *
# esciba aquí la clase TaskList
class TaskList(TaskListBase):
    _total_time_spent = 0  # Variable de clase para almacenar el tiempo total dedicado en todas las listas
    
    def __init__(self):
        super().__init__()
        self._time_spent = 0  # Tiempo dedicado a tareas completadas en esta lista
    
    def task_completed(self, index):
        if self.first is None or index < 0:
            return None
        
        if index == 0:
            task = self.first.value
            self.first = self.first.next
        else:
            prev = None
            current = self.first
            count = 0
            while current is not None and count < index:
                prev = current
                current = current.next
                count += 1
            if current is None:
                return None
            task = current.value
            prev.next = current.next
        
        self._time_spent += task.duration
        TaskList._total_time_spent += task.duration
        return task
    
    @property
    def time_left(self):
        total = 0
        current = self.first
        while current is not None:
            total += current.value.duration
            current = current.next
        return total
    
    @property
    def time_spent(self):
        return self._time_spent
    
    @time_spent.setter
    def time_spent(self, value):
        if value == 0:
            self._time_spent = 0
    
    @classmethod
    def get_total_time_spent(cls):
        return cls._total_time_spent
    
    def get_task_list(self):
        tasks = []
        current = self.first
        while current is not None:
            tasks.append(current.value)
            current = current.next
        return tasks