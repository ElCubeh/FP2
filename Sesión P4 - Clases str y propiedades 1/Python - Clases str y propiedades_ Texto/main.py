"""Ejemplo de uso de la funciones requerida."""

from solution import Texto, Parrafo

poema0 = ['Hola ola', "no te decides"]

poema1 = [
    "La tierra estaba seca.",
    "No había ríos ni fuentes.",
    "Y brotó de tus ojos",
    "el agua, toda el agua."
]
poema2 = [
    "Ante las puertas bien cerradas,",
    "Sobre un río de olvido, va la canción antigua.",
    "Una luz lejos piensa",
    "Como a través de un cielo.",
    "Todos acaso duermen",
    "Mientras él lleva su destino a solas."
]

poemas = []
poemas.append(poema0)
# poemas.append(poema1) # Descomente si quiere probar otro texto
# poemas.append(poema2)  # Descomente si quiere probar otro texto

for poema in poemas:
    print("Texto", poema)
    texto = Texto([Parrafo(ristra) for ristra in poema])
    print("nparrafos:", texto.nparrafos)
    print("npalabras:", texto.npalabras)
    pos = len(poema) // 2
    print(f"get_parrafo {pos}:", end=" ")
    print(texto.get_parrafo(pos).get_str())
    print("Representación informal:")
    print(texto)
    parrafo = "Nuevo párrafo"
    print(f"set_parrafo {pos} {parrafo}")
    texto.set_parrafo(pos, Parrafo(parrafo))
    print(f"get_parrafo {pos}:", end=" ")
    print(texto.get_parrafo(pos).get_str())
    print("nparrafos:", texto.nparrafos)
    print("npalabras:", texto.npalabras)
    print("Representación informal:")
    print(texto)
    print()
