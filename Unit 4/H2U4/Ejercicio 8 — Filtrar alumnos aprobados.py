calificaciones = [9, 5, 7, 10, 4, 6]

aprobadas = list(filter(lambda x: x >= 7, calificaciones))
escala = list(map(lambda x: x * 10, calificaciones))

print("Aprobadas:", aprobadas)
print("Escala:", escala)
