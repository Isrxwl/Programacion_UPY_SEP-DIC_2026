# PPP (Pseudocódigo)
# INPUT
# 1. Leer la temperatura en grados Celsius (C)
# PROCESS
# 2. Calcular Fahrenheit (F) multiplicando C por 9/5 y sumando 32
# OUTPUT
# 3. Mostrar el resultado de la temperatura en Fahrenheit

# Traza a mano (Resultados esperados):
# Para C = 0   -> F = 0 * 9/5 + 32 = 32.0
# Para C = 37  -> F = 37 * 9/5 + 32 = 98.6
# Para C = 100 -> F = 100 * 9/5 + 32 = 212.0

# PPP enfocado a Python (Código funcional)

# INPUT
celsius = float(input("Ingresa la temperatura en Celsius: "))

# PROCESS
fahrenheit = celsius * (9 / 5) + 32

# OUTPUT
print("La temperatura en Fahrenheit es:", fahrenheit)
