with open("origen.txt", "w") as f:
    f.write("linea 1\n")
    f.write("linea 2\n")
    f.write("linea 3\n")

with open("origen.txt", "r") as f_origen, open("respaldo.txt", "w") as f_respaldo:
    for linea in f_origen:
        f_respaldo.write(linea)

with open("respaldo.txt", "r") as f:
    print(f.read(), end="")
