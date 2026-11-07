precios = [120, 45, 300, 80, 15]

con_descuento = list(map(lambda p: p * 0.9, precios))
caros = list(filter(lambda p: p > 100, precios))

print("Con descuento:", con_descuento)
print("Mayores a 100:", caros)
