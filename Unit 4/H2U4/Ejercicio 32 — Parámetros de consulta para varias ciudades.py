import json
import urllib.request
import urllib.parse

ciudades = {
    "Merida": (20.97, -89.62),
    "Cancun": (21.16, -86.85)
}

base_url = "https://api.open-meteo.com/v1/forecast"

for ciudad, (lat, lon) in ciudades.items():
    parametros = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    
    query = urllib.parse.urlencode(parametros)
    url_completa = f"{base_url}?{query}"
    
    with urllib.request.urlopen(url_completa, timeout=10) as respuesta:
        datos = json.loads(respuesta.read().decode("utf-8"))
        temp = datos["current"]["temperature_2m"]
        print(f"Temperatura en {ciudad}: {temp} C")
