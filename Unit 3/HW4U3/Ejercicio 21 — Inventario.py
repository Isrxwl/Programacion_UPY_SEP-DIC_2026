inventario = {"manzana": 50, "pera": 30}
consultas = ["manzana", "uva", "pera", "kiwi"]

for producto in consultas:
    try:
        print(producto, "->", inventario[producto])
    except KeyError:
        print(producto, "-> no disponible")
