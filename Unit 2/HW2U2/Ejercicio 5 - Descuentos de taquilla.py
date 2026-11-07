edad = int(input("Ingresa la edad del comprador: "))
precio_base = 150

if edad < 12:
    precio_final = precio_base - (precio_base * 0.30)
    print("El precio a pagar es", precio_final)
