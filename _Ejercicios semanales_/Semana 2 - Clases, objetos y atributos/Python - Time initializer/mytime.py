

class Time: 
    def __init__(self, hour, minute):
        if not (0 <= hour <= 23):
            raise ValueError("La hora debe estar entre las 0 y las 23")
        if not (0 <= minute <= 59):
            raise ValueError("Los minutos deben estar entre 0 y 59")
        self.hour = hour
        self.minute = minute


t1 = Time(12, 0)
print("Time 1: {}:{}".format(t1.hour, t1.minute))
t2 = Time(8, 54)
print("Time 2: {}:{}".format(t2.hour, t2.minute))
