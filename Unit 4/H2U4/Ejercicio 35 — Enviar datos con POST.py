import json
import urllib.request

datos_diccionario = {"nombre": "Alumno", "matricula": "12345"}
datos_json = json.dumps(datos_diccionario).encode("utf-8")

url = "https://httpbin.org/post" 
req = urllib.request.Request(url, data=datos_json, method="POST")
req.add_header("Content-Type", "application/json")

print("Metodo:", req.method)
print("URL:", req.full_url)
print("Headers:", req.headers)
