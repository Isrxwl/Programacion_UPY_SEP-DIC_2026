# PPP (Pseudocódigo)
# INPUT
# 1. Leer el nombre del usuario
# 2. Leer la edad del usuario y convertirla a número
# PROCESS
# 3. Calcular la edad del próximo año sumando 1 a la edad actual
# OUTPUT
# 4. Mostrar el mensaje de saludo con el nombre y la edad futura
# 5. Mostrar el tipo de dato de la variable nombre
# 6. Mostrar el tipo de dato de la variable edad

# PPP enfocado a Python (Código funcional)

# INPUT
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

# PROCESS
edad_futura = edad + 1
mensaje = f"Hello, {nombre}! Next year you will be {edad_futura}."

# OUTPUT
print(mensaje)
print("El tipo de dato del nombre es:", type(nombre))
print("El tipo de dato de la edad es:", type(edad))
