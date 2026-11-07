import os

# Creamos el archivo de la calculadora
with open("calculadora.py", "w") as f:
    f.write("def sumar(a, b):\n")
    f.write("    return a + b\n\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    print('Prueba:', sumar(2, 3))\n")

print("--- Ejecutando como script principal ---")
os.system("python calculadora.py")

print("\n--- Importando como módulo ---")
import calculadora
print("Usando la función sumar:", calculadora.sumar(10, 5))
