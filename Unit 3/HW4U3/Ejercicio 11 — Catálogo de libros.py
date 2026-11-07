catalogo = [
    {"titulo": "Pedro Paramo", "calif": [5, 4, 5]},
    {"titulo": "Aura", "calif": [3, 4, 4]},
    {"titulo": "Balun Canan", "calif": [5, 5, 5]}
]

mejor_promedio = 0
mejor_libro = ""

for libro in catalogo:
    promedio = sum(libro["calif"]) / len(libro["calif"])
    
    # Imprimimos el titulo y el promedio con 2 decimales
    print(f"{libro['titulo']}: {promedio:.2f}")
    
    # Comprobamos si este libro tiene el mejor promedio hasta ahora
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_libro = libro["titulo"]

print("El mejor es", mejor_libro)
