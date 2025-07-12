# PROBANDO la clase CheckoutQueue:
from supermarket import *

cola = CheckoutQueue()
print(cola) # ➡️None⬅️
cola.enqueue(Client("Ana", 35))
cola.enqueue(Client("Luis", 50))
cola.enqueue(Client("Marta", 25))
print(cola) # ➡️[Ana: 35]->[Luis: 50]->[Marta: 25]⬅️->None
print(cola.dequeue()) # Ana: 35
print(cola.dequeue()) # Luis: 50
print(cola.daily_sales) # 85
print(cola) # ➡️[Marta: 25]⬅️->None

cola.enqueue(Client("José", 40))
cola.enqueue(Client("Laura", 60))
print(cola) # ➡️[Marta: 25]->[José: 40]->[Laura: 60]⬅️->None
nueva_cola = cola.split()
print(cola) # ➡️[Marta: 25]->[Laura: 60]⬅️->None
print(nueva_cola) # ➡️[José: 40]⬅️->None
