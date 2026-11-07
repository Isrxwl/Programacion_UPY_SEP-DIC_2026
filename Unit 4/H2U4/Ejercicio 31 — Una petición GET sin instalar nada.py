import json
import urllib.request

url = ("https://api.open-meteo.com/v1/forecast"
       "?latitude=20.97&longitude=-89.62¤t=temperature_2m")

with urllib.request.urlopen(url, timeout=10) as respuesta:
    print("Estado:", respuesta.status)
    datos = json.loads(respuesta.read().decode("utf-8"))

print("Temperatura actual:", datos["current"]["temperature_2m"], "C")
