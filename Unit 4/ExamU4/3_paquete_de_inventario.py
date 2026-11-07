
import os
import sys
from collections import namedtuple

# PROCESS: Creación del paquete y sus archivos
os.makedirs("inventario", exist_ok=True)

with open("inventario/precios.py", "w", encoding="utf-8") as f:
    f.write("""def con_iva(precio):
    return round(precio * 1.16, 2)

def total_linea(cantidad, precio):
    return cantidad * precio
""")

with open("inventario/reportes.py", "w", encoding="utf-8") as f:
    f.write("""from collections import Counter

def agotados(articulos):
    return [art.nombre for art in articulos if art.stock == 0]

def por_categoria(articulos):
    categorias = [art.categoria for art in articulos]
    return Counter(categorias)
""")

with open("inventario/__init__.py", "w", encoding="utf-8") as f:
    f.write("""from .precios import con_iva, total_linea
from .reportes import agotados, por_categoria
""")

sys.path.insert(0, os.path.abspath('.'))


from inventario import con_iva, total_linea
import inventario.reportes as rep

# INPUT
Articulo = namedtuple("Articulo", ["nombre", "categoria", "precio", "stock"])

articulos = [
    Articulo(nombre="Teclado", categoria="computo", precio=450, stock=3),
    Articulo(nombre="Mouse", categoria="computo", precio=200, stock=0),
    Articulo(nombre="Silla", categoria="oficina", precio=1800, stock=5),
    Articulo(nombre="Lampara", categoria="oficina", precio=350, stock=0),
    Articulo(nombre="Cable", categoria="computo", precio=90, stock=12)
]

# OUTPUT
if __name__ == "__main__":
    for art in articulos:
        precio_final = con_iva(art.precio)
        print(f"El {art.nombre} con IVA queda en {precio_final}")
        
    valor_total = sum(total_linea(art.stock, art.precio) for art in articulos)
    print(f"El valor total del inventario es {valor_total}")
    
    lista_agotados = rep.agotados(articulos)
    print(f"Los agotados son {lista_agotados}")
    
    conteo_categorias = rep.por_categoria(articulos)
    print(f"Conteo por categoría: {conteo_categorias}")
