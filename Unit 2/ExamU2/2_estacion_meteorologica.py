# INPUT
temperatura = float(input("Ingresa la temperatura en Celsius: "))

# PROCESS (Validacion con while)
while temperatura < -50 or temperatura > 60:
    print("Fuera de rango. Intenta de nuevo.")
    temperatura = float(input("Ingresa la temperatura en Celsius: "))

# PROCESS (Clasificacion)
if temperatura < 0:
    categoria = "Helada"
elif temperatura <= 14:
    categoria = "Fria"
elif temperatura <= 29:
    categoria = "Templada"
else:
    categoria = "Calurosa"

# OUTPUT
print(categoria)
