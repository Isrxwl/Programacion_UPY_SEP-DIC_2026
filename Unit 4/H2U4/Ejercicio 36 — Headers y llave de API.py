import urllib.request

API_KEY = "test_key_falsa_999"
url = "https://httpbin.org/get" 

req = urllib.request.Request(url)
req.add_header("Authorization", f"Bearer {API_KEY}")
req.add_header("User-Agent", "MiProgramaPython/1.0")

print("Headers del Request:")
print(req.headers)

print("\nExplicacion:")
print("No conviene escribir la llave directamente en el archivo porque si subes el codigo a un repositorio publico como GitHub, cualquier persona podria robarla y usar la API a tu nombre, agotando tu saldo o causando bloqueos.")
