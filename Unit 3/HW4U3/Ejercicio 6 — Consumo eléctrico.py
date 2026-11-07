consumo = [19, 22, 25, 27, 24, 21]
promedio = sum(consumo) / len(consumo)

for hora, valor in enumerate(consumo):
    if valor > promedio:
        print("Hora", hora, "->", valor, "kWh")
