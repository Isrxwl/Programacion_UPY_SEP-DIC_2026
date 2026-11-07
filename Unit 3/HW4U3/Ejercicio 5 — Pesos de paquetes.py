pesos = [12, 5, 20, 5, 8, 20, 5]

print("Paquetes de 5 kg:", pesos.count(5))
print("Índice del primer 20 kg:", pesos.index(20))

# remove() elimina solo la primera aparición del número
pesos.remove(5)
print("Lista tras quitar un 5 kg:", pesos)

# Ordenamos la lista de mayor a menor (reversa)
pesos.sort(reverse=True)
print("Pesos ordenados (mayor a menor):", pesos)
