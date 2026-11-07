# PPP (Pseudocódigo)
# INPUT
# 1. Leer el valor del ancho del rectángulo
# 2. Leer el valor del alto del rectángulo
# PROCESS
# 3. Calcular el área multiplicando el ancho por el alto
# 4. Calcular el perímetro sumando el doble del ancho más el doble del alto
# OUTPUT
# 5. Mostrar en pantalla el resultado del área y del perímetro

# PPP enfocado a Python (Código funcional)

# INPUT
ancho = float(input("Ingresa el ancho del rectangulo: "))
alto = float(input("Ingresa el alto del rectangulo: "))

# PROCESS
area = ancho * alto
perimetro = (2 * ancho) + (2 * alto)

# OUTPUT
print("El area del rectangulo es:", area)
print("El perimetro del rectangulo es:", perimetro)
