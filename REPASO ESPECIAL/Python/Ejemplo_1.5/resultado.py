# Clases base (Exercise, Node, WorkoutLogBase)

class WorkoutLog(WorkoutLogBase):
    _global_calories_burned = 0

    def __init__(self):
        super().__init__()
        self._total_calories = 0

    def complete_exercise(self, index):
        if index < 0 or index >= self.get_size():
            return None

        exercise_done = None
        if index == 0:
            exercise_done = self.first.value
            self.first = self.first.next
        else:
            prev = self.first
            for _ in range(index - 1):
                prev = prev.next
            exercise_done = prev.next.value
            prev.next = prev.next.next

        self._size -= 1
        if exercise_done:
            self._total_calories += exercise_done.calories_burned
            WorkoutLog._global_calories_burned += exercise_done.calories_burned
        
        return exercise_done

    @property
    def remaining_time(self):
        total = 0
        curr = self.first
        while curr:
            total += curr.value.duration
            curr = curr.next
        return total

    @property
    def total_calories(self):
        return self._total_calories

    @classmethod
    def get_global_calories_burned(cls):
        return cls._global_calories_burned