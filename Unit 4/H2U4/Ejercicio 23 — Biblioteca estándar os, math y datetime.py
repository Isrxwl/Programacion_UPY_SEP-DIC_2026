import os
import math
from datetime import date

# os.path
ruta = os.path.join("respaldos", "reporte.csv")
nombre, extension = os.path.splitext(ruta)
print("Extension:", extension)

# math
print("Raiz cuadrada de 144:", math.sqrt(144))
print("Techo de 7.2:", math.ceil(7.2))

# datetime
fecha_objetivo = date(2026, 3, 15)
fecha_inicio = date(2026, 3, 1)

print("Fecha:", fecha_objetivo.strftime("%d/%m/%Y"))
dias_faltantes = (fecha_objetivo - fecha_inicio).days
print("Faltan:", dias_faltantes, "dias")
