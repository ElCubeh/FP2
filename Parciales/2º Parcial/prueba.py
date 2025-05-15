from networking import InterestGroup

# Creamos dos grupos
group1 = InterestGroup()
group2 = InterestGroup()

print("Inicialmente:")
print(group1)  # ➡️ None
print(group2)  # ➡️ None

# Añadimos miembros al primer grupo
group1.add_member("Ana")
group1.add_member("Luis")
group1.add_member("Marta")

print("\nGrupo 1 tras añadir miembros:")
print(group1)  # ➡️ [Marta]->[Luis]->[Ana]->None

# Añadimos miembros al segundo grupo
group2.add_member("Luis")
group2.add_member("Carlos")
group2.add_member("Elena")

print("\nGrupo 2 tras añadir miembros:")
print(group2)  # ➡️ [Elena]->[Carlos]->[Luis]->None

# Comprobamos si ciertos miembros están en los grupos
print("\nComprobación de miembros:")
print("Luis en grupo1:", group1.is_member("Luis"))  # True
print("Carlos en grupo1:", group1.is_member("Carlos"))  # False
print("Elena en grupo2:", group2.is_member("Elena"))  # True

# Tamaño de los grupos
print("\nTamaño de los grupos:")
print("Grupo1:", group1.size)  # 3
print("Grupo2:", group2.size)  # 3

# Unión de grupos
union_group = group1.union(group2)
print("\nUnión de grupo1 y grupo2:")
print(union_group)  # ➡️ [Ana]->[Luis]->[Marta]->[Carlos]->[Elena]->None

# Probar que no se agregan duplicados
group1.add_member("Luis")  # Ya está
print("\nGrupo1 tras intentar añadir a 'Luis' otra vez:")
print(group1)  # ➡️ [Ana]->[Luis]->[Marta]->None

# Probar que no se elimnan membros
group1.remove_member("Marta")  # Ya está
print("\nGrupo1 tras eliminar 'Marta':")
print(group1)  # ➡️ [Ana]->[Luis]->None
