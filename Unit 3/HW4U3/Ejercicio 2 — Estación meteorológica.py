temperaturas = [31, 33, 30, 28, 34, 35, 29, 27, 32, 36]

# Guardamos el primer y ultimo dia en variables usando sus indices
primer_dia = temperaturas[0]
ultimo_dia = temperaturas[-1] # Usamos -1 para no escribir el numero 10

# 1. Imprime la temperatura del ultimo dia
print("Último día:", ultimo_dia)

# 2. Promedio del primer y ultimo dia
promedio = (primer_dia + ultimo_dia) / 2
print("Promedio:", promedio)

# 3. Booleano: ¿El ultimo dia fue mas caluroso que el primero?
fue_mas_caluroso = ultimo_dia > primer_dia
print("¿Último más caluroso?:", fue_mas_caluroso)
