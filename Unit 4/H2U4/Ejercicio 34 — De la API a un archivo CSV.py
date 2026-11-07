import csv
import json

respuesta = ('{"ventas": ['
             '{"producto": "Lapiz", "unidades": 10, "precio": 5},'
             '{"producto": "Cuaderno", "unidades": 3, "precio": 30}]}')

datos = json.loads(respuesta)

with open("ventas_api.csv", "w", newline="") as f:
    columnas = ["producto", "unidades", "precio", "total"]
    w = csv.DictWriter(f, fieldnames=columnas)
    w.writeheader()
    
    for venta in datos["ventas"]:
        venta["total"] = venta["unidades"] * venta["precio"]
        w.writerow(venta)

# Comprobamos
with open("ventas_api.csv", "r") as f:
    print(f.read())
