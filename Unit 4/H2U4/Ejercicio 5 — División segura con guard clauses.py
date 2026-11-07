def dividir(a, b):
    if b == 0:
        return "no se puede dividir entre cero"
    return a / b

pruebas = [(10, 2), (9, 0), (7, 7)]

for a, b in pruebas:
    print(dividir(a, b))
