with open("temperaturas.txt", "w") as f:
    f.write("18\n25\n30\n22\n19\n")

with open("temperaturas.txt", "r") as f:
    lineas = f.readlines()

temperaturas = [int(x) for x in lineas]
print("Cantidad:", len(temperaturas))
print("Maxima:", max(temperaturas))
