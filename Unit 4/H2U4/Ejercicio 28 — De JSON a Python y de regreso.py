import json

texto = '{"temp": 34.5, "lluvia": false, "horas": [1, 2, 3]}'
datos = json.loads(texto)

print("Tipo:", type(datos).__name__)
print("Temp:", datos["temp"], "->", type(datos["temp"]).__name__)
print("Lluvia:", datos["lluvia"], "->", type(datos["lluvia"]).__name__)
print("Horas:", datos["horas"], "->", type(datos["horas"]).__name__)

datos["temp"] = 35.0
print("JSON de regreso:", json.dumps(datos))
