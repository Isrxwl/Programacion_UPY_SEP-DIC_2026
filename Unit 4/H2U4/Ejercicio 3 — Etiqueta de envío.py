def etiqueta(producto, destino="Merida", urgente=False):
    return f"Producto: {producto} | Destino: {destino} | Urgente: {urgente}"

# Llamadas para comprobar los valores por defecto
print(etiqueta("Laptop"))
print(etiqueta("Monitor", destino="Cancun"))
print(etiqueta("Teclado", urgente=True))
