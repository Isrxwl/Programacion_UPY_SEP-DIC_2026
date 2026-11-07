with open("notas.txt", "w") as f:
    f.write("Ana 9\n")
    f.write("Luis 6\n")
    f.write("Mia 8\n")
    f.write("Beto 5\n")

with open("notas.txt", "r") as f:
    for linea in f:
        partes = linea.split()
        nombre = partes[0]
        calificacion = int(partes[1])
        
        if calificacion >= 8:
            print(nombre)
