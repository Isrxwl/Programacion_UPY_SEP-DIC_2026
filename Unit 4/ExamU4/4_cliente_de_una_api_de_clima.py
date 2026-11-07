
import urllib.parse
import json
import logging
import os

# Borramos el log 
if os.path.exists("api.log"):
    os.remove("api.log")

# Configuración básica para que los errores se guarden en el archivo
logging.basicConfig(filename='api.log', level=logging.ERROR, format='%(message)s')

# INPUT
exitosa = '{"daily": {"temperature_2m_max": [33.4, 31.2, 29.8]}}'
rota = '{"daily": {"temperature'
peticiones_procesadas = 0

# PROCESS
def armar_url(latitud, longitud, dias=3):
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "daily": "temperature_2m_max",
        "forecast_days": dias
    }
    
    query_string = urllib.parse.urlencode(parametros)
    return f"https://api.open-meteo.com/v1/forecast?{query_string}"

def clasificar_estado(codigo):
    
    # Usamos división entera entre 100 para sacar la centena del código HTTP
    centena = codigo // 100
    if centena == 2:
        return "exito"
    if centena == 3:
        return "redireccion"
    if centena == 4:
        return "error del cliente"
    if centena == 5:
        return "error del servidor"
    return "desconocido"

def procesar(codigo, cuerpo):
    global peticiones_procesadas
    try:
        estado = clasificar_estado(codigo)
        if estado != "exito":
            raise ValueError(f"la API respondio {codigo}")
        
        # Si es éxito, pasamos el JSON de texto a diccionario
        datos = json.loads(cuerpo)
        temperaturas_maximas = datos["daily"]["temperature_2m_max"]
        
        # Devolvemos la temperatura más alta de la lista
        return max(temperaturas_maximas)
        
    except json.JSONDecodeError as e:
        
        logging.error(f"Error de JSON invalido: {e}")
        return None
    except ValueError as e:
        
        logging.error(f"Error de estado invalido: {e}")
        return None
    finally:
        
        peticiones_procesadas += 1

# OUTPUT
url_merida = armar_url(20.97, -89.62)
print(f"URL de Mérida: {url_merida}")

res1 = procesar(200, exitosa)
res2 = procesar(404, exitosa)
res3 = procesar(200, rota)

print(f"Resultado de llamada 1: {res1}")
print(f"Resultado de llamada 2: {res2}")
print(f"Resultado de llamada 3: {res3}")
print(f"Total de peticiones procesadas: {peticiones_procesadas}")

print("\n--- Contenido de api.log ---")
with open("api.log", "r") as log_file:
    print(log_file.read().strip())
