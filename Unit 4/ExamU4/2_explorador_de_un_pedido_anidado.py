
# INPUT
pedido = {"folio": "A-100",
          "contenido": [
              {"producto": "Teclado", "precio": 450},
              {"paquete": "Oficina", "contenido": [
                  {"producto": "Mouse", "precio": 200},
                  {"producto": "Monitor", "precio": 3200},
                  {"paquete": "Cables", "contenido": [
                      {"producto": "HDMI", "precio": 150},
                      {"producto": "USB", "precio": 90}]}]},
              {"producto": "Silla", "precio": 1800}]}

# PROCESS
def contar_productos(obj):
    
    # Caso base
    if not isinstance(obj, (dict, list)):
        return 0
    
    # Caso recursivo: 
    total = 0
    if isinstance(obj, dict):
        if "producto" in obj:
            total += 1
        for valor in obj.values():
            total += contar_productos(valor)
    elif isinstance(obj, list):
        for elemento in obj:
            total += contar_productos(elemento)
    return total

def total_precio(obj):
    
    # Caso base: tipos de datos simples 
    if not isinstance(obj, (dict, list)):
        return 0
    
    # Caso recursivo: sumar precios encontrados
    total = 0
    if isinstance(obj, dict):
        if "precio" in obj:
            total += obj["precio"]
        for valor in obj.values():
            total += total_precio(valor)
    elif isinstance(obj, list):
        for elemento in obj:
            total += total_precio(elemento)
    return total

def buscar_clave(obj, clave):
    
    # Caso base: Devolvemos una lista vacía
    if not isinstance(obj, (dict, list)):
        return []
    
    # Caso recursivo: recolectar coincidencias
    resultados = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == clave:
                resultados.append(v)
            resultados.extend(buscar_clave(v, clave))
    elif isinstance(obj, list):
        for elemento in obj:
            resultados.extend(buscar_clave(elemento, clave))
    return resultados

def profundidad(obj):
    # Caso base: los datos primitivos (int, str) no añaden profundidad (nivel 0)
    if not isinstance(obj, (dict, list)):
        return 0
    
    # Caso recursivo: cada diccionario o lista añade 1 nivel más
    max_profundidad_hijos = 0
    if isinstance(obj, dict):
        for valor in obj.values():
            prof = profundidad(valor)
            if prof > max_profundidad_hijos:
                max_profundidad_hijos = prof
    elif isinstance(obj, list):
        for elemento in obj:
            prof = profundidad(elemento)
            if prof > max_profundidad_hijos:
                max_profundidad_hijos = prof
                
    return 1 + max_profundidad_hijos

# OUTPUT
print(f"Hay {contar_productos(pedido)} productos.")
print(f"El total es {total_precio(pedido)}.")

paquetes = buscar_clave(pedido, "paquete")
print(f"Los paquetes son {paquetes}.")

print(f"La profundidad es {profundidad(pedido)}.")

nombres_productos = buscar_clave(pedido, "producto")
print(f"Nombres de los productos: {nombres_productos}")
