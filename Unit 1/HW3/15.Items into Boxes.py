# PPP (Pseudocódigo)
# INPUT
# 1. Leer el número total de artículos
# 2. Leer la capacidad de cada caja
# PROCESS
# 3. Calcular las cajas llenas usando división entera (total artículos DIV capacidad caja)
# 4. Calcular los artículos sobrantes usando módulo (total artículos MOD capacidad caja)
# OUTPUT
# 5. Mostrar la cantidad de cajas llenas y los artículos que sobran

# Traza a mano (Resultado esperado para 30 artículos y cajas de 4):
# Artículos = 30, Capacidad = 4
# Cajas llenas = 30 // 4 = 7
# Sobrantes = 30 % 4 = 2
# Resultado esperado: 7 cajas llenas, sobran 2

# PPP enfocado a Python (Código funcional)

# INPUT
articulos = int(input("Ingresa el numero total de articulos: "))
capacidad = int(input("Ingresa la capacidad de la caja: "))

# PROCESS
cajas_llenas = articulos // capacidad
sobrantes = articulos % capacidad

# OUTPUT
print(f"Cajas llenas armadas: {cajas_llenas}")
print(f"Articulos que sobran: {sobrantes}")
