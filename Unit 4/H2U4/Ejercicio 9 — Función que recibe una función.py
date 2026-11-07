def aplicar(numeros, operacion):
    resultado = []
    for n in numeros:
        resultado.append(operacion(n))
    return resultado

lista = [1, 2, 3, 4]

print(aplicar(lista, lambda x: x ** 2))
print(aplicar(lista, lambda x: x * 2))
print(aplicar(lista, str))
