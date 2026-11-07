import urllib.request
from urllib.error import HTTPError, URLError

def pedir(url):
    try:
        with urllib.request.urlopen(url, timeout=3) as respuesta:
            print(f"Exito: la URL {url} devolvio {respuesta.status}")
    except HTTPError as e:
        print(f"Error HTTP en {url}: codigo {e.code}")
    except URLError as e:
        if isinstance(e.reason, TimeoutError):
            print(f"TimeoutError en {url}: se agoto el tiempo")
        else:
            print(f"URLError en {url}: no hubo conexion ({e.reason})")
    except TimeoutError:
        print(f"TimeoutError en {url}: se agoto el tiempo")

# Pruebas
pedir("https://api.open-meteo.com/v1/forecast?latitude=20.97&longitude=-89.62¤t=temperature_2m")
pedir("https://api.open-meteo.com/v1/forecast/noexiste")
pedir("https://un-dominio-inventado-que-no-existe-123.com")
