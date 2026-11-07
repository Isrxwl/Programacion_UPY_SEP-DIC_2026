intentos = 0

def sumar_intento():
    global intentos
    intentos += 1

def mostrar():
    intentos = 10  # Variable local
    print("Intentos (local):", intentos)

sumar_intento()
sumar_intento()
sumar_intento()

mostrar()
print("Intentos (global):", intentos)
