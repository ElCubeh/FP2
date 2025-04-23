# Puede modificar el presente fichero para probar otros casos
print("(Ejecución del fichero modificable prueba.py)")

# Función auxiliar que, dado un contenedor, muestra partiendo de first
# el valor en los nodos de la lista entre paréntesis
def show(cont):
    act = cont.first
    if not act:
        print("La lista está vacía")
    while act:
        print(f"({act.value})", end="")
        act = act.next
        if act:
            print(" -> ")
        else:
            print()

# PROBANDO la clase Container:
from container import Container
# 1. Construye un contenedor (vacío) y lo muestra
contenedor = Container()
show(contenedor)
print("Tamaño:", contenedor.size)
# 2. Inserta varios elementos y muestra el contenido resultante
contenedor.insert("uno")
contenedor.insert(2)
contenedor.insert("dos")
contenedor.insert(1)
contenedor.insert(2)
contenedor.insert("tres")
show(contenedor)
print("Tamaño:", contenedor.size)
print("Unico dos:", contenedor.find_unique("dos"))
print("Unico 2:", contenedor.find_unique("2"))
print("Unico 1:", contenedor.find_unique("1"))
# 3. Muestra el contenedor tras delete()
contenedor.delete_all(2)
show(contenedor)
