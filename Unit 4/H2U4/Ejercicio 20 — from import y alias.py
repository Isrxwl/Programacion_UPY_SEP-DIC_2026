# Creamos el archivo utilitario
with open("texto_utils.py", "w") as f:
    f.write("def mayusculas(t):\n")
    f.write("    return t.upper()\n\n")
    f.write("def contar_palabras(t):\n")
    f.write("    return len(t.split())\n")

# Importamos de las maneras solicitadas
import texto_utils
from texto_utils import mayusculas
import texto_utils as tu

frase = "hola mundo desde python"

print(texto_utils.mayusculas(frase))
print(mayusculas(frase))
print(tu.contar_palabras(frase), "palabras")
