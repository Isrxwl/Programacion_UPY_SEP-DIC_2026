
with open("calculos.py", "w") as f:
    f.write("def promedio(datos):\n")
    f.write("    return sum(c for n, c in datos) / len(datos)\n\n")
    f.write("def aprobados(datos):\n")
    f.write("    return [n for n, c in datos if c >= 7]\n")

with open("reporte.py", "w") as f:
    f.write("import calculos\n\n")
    f.write("def imprimir(datos):\n")
    f.write("    print('Promedio:', round(calculos.promedio(datos), 2))\n")
    f.write("    print('Aprobados:', calculos.aprobados(datos))\n")

import reporte

datos = [("Ana", 9), ("Luis", 6), ("Mia", 8)]
reporte.imprimir(datos)
