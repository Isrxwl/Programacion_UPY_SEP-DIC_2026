# PPP (Pseudocódigo)
# INPUT
# 1. Leer el número total de segundos
# PROCESS
# 2. Calcular las horas usando división entera (total de segundos DIV 3600)
# 3. Calcular los segundos sobrantes usando módulo (total de segundos MOD 3600)
# 4. Calcular los minutos usando división entera (segundos sobrantes DIV 60)
# 5. Calcular los segundos finales usando módulo (segundos sobrantes MOD 60)
# OUTPUT
# 6. Mostrar el resultado en formato de horas, minutos y segundos

# Traza a mano (Resultado esperado):
# Total = 3661
# Horas = 3661 // 3600 = 1
# Sobrantes = 3661 % 3600 = 61
# Minutos = 61 // 60 = 1
# Segundos finales = 61 % 60 = 1
# Resultado esperado: 1h 1m 1s

# PPP enfocado a Python (Código funcional)

# INPUT
total_segundos = int(input("Ingresa el total de segundos: "))

# PROCESS
horas = total_segundos // 3600
sobrantes = total_segundos % 3600
minutos = sobrantes // 60
segundos = sobrantes % 60

# OUTPUT
print(f"{horas}h {minutos}m {segundos}s")
