config = {
    "app": {
        "db": {"host": "local", "port": 5432},
        "logs": [{"nivel": "info"}, {"port": 9000}]
    }
}

def buscar(obj, clave):
    resultados = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == clave:
                resultados.append(v)
            resultados.extend(buscar(v, clave))
    elif isinstance(obj, list):
        for elemento in obj:
            resultados.extend(buscar(elemento, clave))
    return resultados

print(buscar(config, "port"))
