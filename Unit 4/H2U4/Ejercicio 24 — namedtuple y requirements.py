from collections import namedtuple

Producto = namedtuple("Producto", ["nombre", "precio", "stock"])

productos = [
    Producto("Laptop", 15000, 5),
    Producto("Mouse", 300, 20),
    Producto("Monitor", 3500, 10)
]

for p in productos:

    print(f"Producto: {p.nombre}, Precio: ${p.precio}")
  
with open("requirements.txt", "w") as f:
    f.write("requests==2.31.0\n")
    f.write("pandas==2.2.0\n")

print("\n--- Contenido del requirements.txt ---")
with open("requirements.txt", "r") as f:
    print(f.read())
