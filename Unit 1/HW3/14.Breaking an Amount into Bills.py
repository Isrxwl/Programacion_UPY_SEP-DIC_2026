# PPP (Pseudocódigo)
# INPUT
# 1. Leer una cantidad entera en pesos
# PROCESS
# 2. Calcular los billetes de $500 usando división entera (cantidad DIV 500)
# 3. Calcular el restante usando módulo (cantidad MOD 500)
# 4. Calcular los billetes de $100 usando división entera (restante DIV 100)
# 5. Calcular el nuevo restante usando módulo (restante MOD 100)
# 6. Calcular los billetes de $20 usando división entera (nuevo restante DIV 20)
# 7. Calcular el sobrante final usando módulo (nuevo restante MOD 20)
# OUTPUT
# 8. Mostrar la cantidad de billetes de cada denominación y el dinero sobrante

# Traza a mano (Resultado esperado para 1270):
# Cantidad = 1270
# Billetes de 500 = 1270 // 500 = 2
# Restante = 1270 % 500 = 270
# Billetes de 100 = 270 // 100 = 2
# Restante = 270 % 100 = 70
# Billetes de 20 = 70 // 20 = 3
# Sobrante = 70 % 20 = 10
# Resultado esperado: 2 de 500, 2 de 100, 3 de 20 y sobran 10

# PPP enfocado a Python (Código funcional)

# INPUT
cantidad = int(input("Ingresa la cantidad entera en pesos: "))

# PROCESS
billetes_500 = cantidad // 500
restante = cantidad % 500

billetes_100 = restante // 100
restante = restante % 100

billetes_20 = restante // 20
sobrante = restante % 20

# OUTPUT
print(f"Billetes de $500: {billetes_500}")
print(f"Billetes de $100: {billetes_100}")
print(f"Billetes de $20: {billetes_20}")
print(f"Sobran: {sobrante}")
