operaciones = [("8","2"), ("9","0"), ("a","3"), ("6","3")]

validas = 0
division_cero = 0
datos_invalidos = 0

for n1, n2 in operaciones:
    try:
        resultado = int(n1) / int(n2)
        validas += 1
    except ZeroDivisionError:
        division_cero += 1
    except ValueError:
        datos_invalidos += 1

print(validas, "validas")
print(division_cero, "division entre cero")
print(datos_invalidos, "dato invalido")
