anio = int(input("Ingresa un ano: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Ano bisiesto")
else:
    print("No es ano bisiesto")
