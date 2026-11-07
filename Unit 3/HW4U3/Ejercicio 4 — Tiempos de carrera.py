tiempos = [58.2, 61.0, 55.4, 59.9, 57.1]

print("Corredores:", len(tiempos))
print("Más rápido:", min(tiempos))
print("Más lento:", max(tiempos))

# sorted() ordena de menor a mayor (más rápido a más lento) sin tocar la lista original
print("Ordenados (rápido a lento):", sorted(tiempos))
print("Lista original:", tiempos)
