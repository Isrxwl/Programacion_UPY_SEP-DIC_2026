 
# INPUT
grupo = [9, 5, 7, 10, 4, 6, 8, 9]
revisadas = 0

# PROCESS
def estadisticas(datos):
    minima = min(datos)
    maxima = max(datos)
    promedio = round(sum(datos) / len(datos), 2)
    return minima, maxima, promedio

def clasificar(calificacion):
    global revisadas
    revisadas += 1
    
    if calificacion >= 9:
        return "excelente"
    if calificacion >= 7:
        return "aprobado"
    return "reprobado"

def aprobados(datos, minimo=7):
    return list(filter(lambda x: x >= minimo, datos))

# OUTPUT
minima, maxima, promedio = estadisticas(grupo)

print(f"La calificación mínima es: {minima}")
print(f"La calificación máxima es: {maxima}")
print(f"El promedio es: {promedio}")

aprobados_defecto = aprobados(grupo)
print(f"Aprobados (mínimo por defecto): {aprobados_defecto}")

aprobados_9 = aprobados(grupo, minimo=9)
print(f"Aprobados (mínimo 9): {aprobados_9}")

escala_100 = list(map(lambda x: x * 10, grupo))
print(f"Calificaciones en escala de 100: {escala_100}")

clasificaciones = [clasificar(nota) for nota in grupo]
print(f"Clasificación de cada nota: {clasificaciones}")

print(f"La función 'clasificar' se llamó {revisadas} veces.")
