import logging

# Configuramos el archivo, el nivel y el formato nivel - msj
logging.basicConfig(filename="errores.log", level=logging.ERROR, format="%(levelname)s - %(message)s", filemode="w")

lecturas = ["21", "35", "xx", "40"]
validas = 0

for lectura in lecturas:
    try:
        valor = int(lectura)
        validas += 1
    except ValueError:
        # Registramos el error en lugar de usar print
        logging.error(f"lectura invalida: {lectura}")

# Mostramos el contenido del archivo log
with open("errores.log", "r") as f:
    print(f.read(), end="")

# Mostramos cuántas fueron válidas
print(f"hay {validas} lecturas validas.")
