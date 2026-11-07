from collections import Counter, defaultdict

# Parte 1: Counter
lenguajes = ["python", "java", "python", "go", "java", "python"]
conteo = Counter(lenguajes)

print("Conteo:", conteo)
print("Mas comun:", conteo.most_common(1))

# Parte 2: defaultdict
inscripciones = [("Ana", "Mate"), ("Luis", "Fisica"), ("Ana", "Quimica")]
por_alumno = defaultdict(list)

for alumno, materia in inscripciones:
    por_alumno[alumno].append(materia) 

print("Ana:", por_alumno["Ana"])
print("Luis:", por_alumno["Luis"])
