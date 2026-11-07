import sys
import os

print("Version de Python:", sys.version.split()[0])
print("Ruta del interprete:", sys.executable)
print("¿Existe la carpeta venv?:", os.path.exists("venv"))

# Generamos el archivo con los comandos
with open("pasos.txt", "w") as f:
    f.write("python -m venv venv\n")
    f.write("source venv/bin/activate  # o venv\\Scripts\\activate en Windows\n")
    f.write("pip install requests\n")
    f.write("pip freeze > requirements.txt\n")

print("\n--- Contenido de pasos.txt ---")
with open("pasos.txt", "r") as f:
    print(f.read())
