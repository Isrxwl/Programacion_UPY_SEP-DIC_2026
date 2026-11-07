def procesar_pedido(stock, cantidad):
    if cantidad <= 0:
        raise ValueError("cantidad debe ser positiva")
    if cantidad > stock:
        faltan = cantidad - stock
        raise ValueError(f"faltan {faltan} unidades")

pedidos = [(100, 30), (100, 500), (100, 0)]
exitosos = 0

for stock, cantidad in pedidos:
    try:
        procesar_pedido(stock, cantidad)
        exitosos += 1
    except ValueError as e:
        print(e)

print(exitosos, "pedido exitoso")
