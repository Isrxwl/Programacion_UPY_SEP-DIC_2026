import os

# Creamos la carpeta y los archivos del paquete
os.makedirs("tienda", exist_ok=True)

with open("tienda/__init__.py", "w") as f:
    f.write("")

with open("tienda/precios.py", "w") as f:
    f.write("def con_iva(p):\n")
    f.write("    return round(p * 1.16, 2)\n")

with open("tienda/envios.py", "w") as f:
    f.write("def costo(kg):\n")
    f.write("    return kg * 25\n")

# Ahora los importamos y los usamos
from tienda.precios import con_iva
from tienda.envios import costo

precio = con_iva(100)
envio = costo(2)

print("Precio con IVA:", precio)
print("Envio:", envio)
print("Total:", precio + envio)
