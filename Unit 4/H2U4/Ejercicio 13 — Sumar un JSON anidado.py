datos = {"a": 1, "b": {"c": 2, "d": [3, 4, {"e": 5}]}}

def suma_profunda(obj):
    if isinstance(obj, dict):
        return sum(suma_profunda(valor) for valor in obj.values())
    if isinstance(obj, list):
        return sum(suma_profunda(elemento) for elemento in obj)
    return obj

print("Total:", suma_profunda(datos))
