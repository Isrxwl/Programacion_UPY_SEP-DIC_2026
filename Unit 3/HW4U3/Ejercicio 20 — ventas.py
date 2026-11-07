import csv

# 1. Crear el archivo original
with open("ventas.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["producto", "unidades", "precio"])
    w.writerow(["Lapiz", 10, 5])
    w.writerow(["Cuaderno", 3, 30])

# 2. Leer, calcular el total y escribir en el nuevo archivo
with open("ventas.csv", "r") as f_in, open("reporte.csv", "w", newline="") as f_out:
    lector = csv.DictReader(f_in)
    
    # Creamos el nuevo encabezado agregando 'total'
    campos_nuevos = lector.fieldnames + ["total"]
    escritor = csv.DictWriter(f_out, fieldnames=campos_nuevos)
    
    escritor.writeheader()
    
    for fila in lector:
        # Calculamos el total multiplicando unidades por precio
        total = int(fila["unidades"]) * int(fila["precio"])
        # Añadimos el valor al diccionario de la fila
        fila["total"] = total
        # Escribimos la fila completa en el nuevo archivo
        escritor.writerow(fila)

# 3. Mostrar el reporte para comprobar
with open("reporte.csv", "r") as f:
    print(f.read(), end="")
