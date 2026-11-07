# PPP (Pseudocódigo)
# INPUT
# 1. Leer la velocidad en km/h
# 2. Leer el tiempo en horas
# PROCESS
# 3. Calcular la distancia multiplicando la velocidad por el tiempo
# OUTPUT
# 4. Mostrar el resultado de la distancia recorrida

# Traza a mano (Resultado esperado):
# Velocidad = 60, Tiempo = 2.5 -> Distancia = 60 * 2.5 = 150.0

# PPP enfocado a Python (Código funcional)

# INPUT
speed = float(input("Ingresa la velocidad en km/h: "))
time = float(input("Ingresa el tiempo en horas: "))

# PROCESS
distance = speed * time

# OUTPUT
print("La distancia recorrida es:", distance)
