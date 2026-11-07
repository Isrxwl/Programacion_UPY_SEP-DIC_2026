def estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

lecturas = [18, 25, 30, 22, 19]
minimo, maximo, promedio = estadisticas(lecturas)

print("Minimo:", minimo)
print("Maximo:", maximo)
print("Promedio:", round(promedio, 2))
