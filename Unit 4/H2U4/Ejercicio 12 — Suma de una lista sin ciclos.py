def suma_lista(numeros):
    if not numeros: # Si la lista está vacía
        return 0
    return numeros[0] + suma_lista(numeros[1:])

print(suma_lista([1, 2, 3, 4, 5]))
