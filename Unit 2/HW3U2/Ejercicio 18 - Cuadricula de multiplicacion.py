n = int(input("Ingresa N: "))

for renglon in range(1, n + 1):
    for columna in range(1, n + 1):
        producto = renglon * columna
        # end="\t" pone un espacio largo (tabulador) para que se vea como cuadricula
        print(producto, end="\t")
    
    # Este print vacio hace el salto a la siguiente linea cuando termina un renglon
    print()
