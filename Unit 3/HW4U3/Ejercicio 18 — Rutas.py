import os

archivo = "foto.jpg"

# splitext separa "foto" de ".jpg"
nombre_sin_extension = os.path.splitext(archivo)[0]

# Construimos la nueva ruta
ruta_respaldo = os.path.join("respaldos", nombre_sin_extension + ".bak")

ruta_respaldo = ruta_respaldo.replace("\\", "/")

existe_original = os.path.exists(archivo)

print("Respaldo:", ruta_respaldo, "y Original existe:", existe_original)
