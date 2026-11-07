# PPP (Pseudocódigo)
# INPUT
# 1. Leer la cantidad en dólares (amount)
# 2. Leer el tipo de cambio de pesos por dólar (rate)
# PROCESS
# 3. Calcular la cantidad en pesos multiplicando los dólares por el tipo de cambio
# OUTPUT
# 4. Mostrar la cantidad convertida en pesos

# Traza a mano (Resultado esperado):
# Dólares (amount) = 100, Tipo de cambio (rate) = 18.5 -> Pesos = 100 * 18.5 = 1850.0

# PPP enfocado a Python (Código funcional)

# INPUT
amount = float(input("Ingresa la cantidad en dolares: "))
rate = float(input("Ingresa el tipo de cambio (pesos por dolar): "))

# PROCESS
pesos = amount * rate

# OUTPUT
print("La cantidad en pesos es:", pesos)
