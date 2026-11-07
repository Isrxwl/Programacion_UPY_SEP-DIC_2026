# Explicación del error (Bug):
# Cuando usamos input(), Python siempre guarda lo que escribimos como texto (tipo 'str'). 
# Entonces, si escribimos 5, la variable 'x' no guarda el número 5, sino el texto "5".
# En Python, si multiplicas un texto por un número (ej. "5" * 2), el programa no hace una operación matemática, sino que repite el texto dos veces, dando como resultado "55".

# PPP enfocado a Python corregido (Código funcional)

# INPUT
# Solución: Convertir el texto a número entero usando int() en el mismo momento que se lee
x = int(input("Enter a number: "))

# PROCESS
# Ahora sí se hace una multiplicación matemática porque x es de tipo int
resultado = x * 2

# OUTPUT
print(resultado)
