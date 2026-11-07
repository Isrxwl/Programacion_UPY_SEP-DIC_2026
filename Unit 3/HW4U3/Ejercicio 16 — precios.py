productos = [("Lapiz", 5), ("Cuaderno", 30), ("Goma", 8)]

with open("precios.txt", "w") as f:
    f.write("PRODUCTO PRECIO\n")
    for nombre, precio in productos:
        f.write(nombre + " " + str(precio) + "\n")

with open("precios.txt", "r") as f:
    print(f.read())
