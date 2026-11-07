color = input("Color del semaforo: ").lower()

if color == "rojo":
    print("Alto")
elif color == "amarillo":
    print("Reduce la velocidad")
elif color == "verde":
    print("Avanza")
else:
    print("Color invalido")
