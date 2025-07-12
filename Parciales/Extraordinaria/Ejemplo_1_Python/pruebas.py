from tasks import *
from tasklist import TaskList

t1 = Task("Lavar los platos", 15)
t2 = Task("Hacer la compra", 40)
t3 = Task("Estudiar Java", 120)
t4 = Task("Ejercicio", 60)
t5 = Task("Estudiar Python", 150)

lista1 = TaskList()
lista2 = TaskList()

lista1.add_task(t1)
lista1.add_task(t2)
lista1.add_task(t3)
lista1.add_task(t4)
lista2.add_task(t5)

print("lista1 actual:", lista1)

print("\nTarea en la posición 1:", lista1.get_task(1)) # Esperado: Hacer la compra: 40 min

# Tiempo total pendiente
print("\nTiempo pendiente:", lista1.time_left) # Esperado: 235

# Completar tarea en la posición 1
print("\nTarea completada (posición 1):", lista1.task_completed(1)) # Esperado: Hacer la compra: 40 min

# Mostrar lista1 después de completar una tarea
print("\nlista1 después de completar una tarea:", lista1)

# Tiempo restante y tiempo invertido
print("\nTiempo restante: ", lista1.time_left) # Esperado: 195
print("Tiempo invertido: ", lista1.time_spent) # Esperado: 40

# Tarea en posición inválida
print("\nIntento de acceder a tarea en posición inválida: ", lista1.get_task(10)) # Esperado: null

# Completar todas las tareas restantes
while (lista1.time_left > 0):
    print("Tarea completada:", lista1.task_completed(0))

# Estado final
print("\nlista1 vacía:", lista1)
print("Tiempo invertido:", lista1.time_spent) # Esperado: suma
print("Tiempo total invertido:", TaskList.get_total_time_spent()) # Esperado: suma total
print("Tarea completada en lista 2:", lista2.task_completed(0))
print("Tiempo total invertido:", TaskList.get_total_time_spent()) # Esperado: suma total

lista1.add_task(t1)
lista1.add_task(t2)
lista1.add_task(t3)
print("Lista de tareas como list:", lista1.get_task_list()) # List de Python
