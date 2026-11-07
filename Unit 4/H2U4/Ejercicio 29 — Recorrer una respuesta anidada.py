import json

respuesta_api = '{"total": 3, "resultados": [{"nombre": "Ana", "ciudad": "Merida"}, {"nombre": "Luis", "ciudad": "Cancun"}, {"nombre": "Mia", "ciudad": "Merida"}]}'

datos = json.loads(respuesta_api)

print("Total:", datos["total"])

nombres = []
nombres_merida = []

for resultado in datos["resultados"]:
    nombres.append(resultado["nombre"])
    if resultado["ciudad"] == "Merida":
        nombres_merida.append(resultado["nombre"])

print("Todos los nombres:", ", ".join(nombres))
print("De Merida son:", " y ".join(nombres_merida))
