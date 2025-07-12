from tasks import TaskList
from tasks import Task

t1 = Task("Lavar los platos", 15)
t2 = Task("Hacer la compra", 40)
t3 = Task("Estudiar Python", 120)

lista = TaskList()
lista.add_task(t1)
lista.add_task(t2)
lista.add_task(t3)
print(lista) # ➡️[Lavar los platos: 15 min]->[Hacer la compra: 40 min]->[Estudiar Python: 120 min]->None

print(lista.get_task(1))       # Hacer la compra: 40 min
print(lista.time_left)         # 175

print(lista.task_completed(1)) # Hacer la compra: 40 min
print(lista) # ➡️[Lavar los platos: 15 min]->[Estudiar Python: 120 min]->None
print(lista.time_left)         # 135
print(lista.time_spent)        # 40