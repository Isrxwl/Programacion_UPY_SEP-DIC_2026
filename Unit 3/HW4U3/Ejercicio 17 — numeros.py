# Crear el archivo original
with open("numeros.txt", "w") as f:
    f.write("3\n8\n5\n10\n7\n2\n")

# Leer el original y escribir en el de pares
with open("numeros.txt", "r") as f_in, open("pares.txt", "w") as f_out:
    for linea in f_in:
        numero = int(linea)
        if numero % 2 == 0:
            f_out.write(str(numero) + "\n")

# Mostrar el resultado final
with open("pares.txt", "r") as f:
    print(f.read(), end="")
