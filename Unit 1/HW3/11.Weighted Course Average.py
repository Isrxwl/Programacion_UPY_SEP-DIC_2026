# PPP (Pseudocódigo)
# INPUT
# 1. Leer la calificación del Proyecto
# 2. Leer la calificación del Examen
# 3. Leer la calificación de la Tarea
# PROCESS
# 4. Multiplicar la calificación del Proyecto por 0.40 (40%)
# 5. Multiplicar la calificación del Examen por 0.30 (30%)
# 6. Multiplicar la calificación de la Tarea por 0.30 (30%)
# 7. Sumar los tres resultados anteriores para obtener el promedio ponderado
# OUTPUT
# 8. Mostrar la calificación final ponderada

# PPP enfocado a Python (Código funcional)

# INPUT
proyecto = float(input("Ingresa la calificacion del Proyecto: "))
examen = float(input("Ingresa la calificacion del Examen: "))
tarea = float(input("Ingresa la calificacion de la Tarea: "))

# PROCESS
ponderacion_proyecto = proyecto * 0.40
ponderacion_examen = examen * 0.30
ponderacion_tarea = tarea * 0.30

calificacion_final = ponderacion_proyecto + ponderacion_examen + ponderacion_tarea

# OUTPUT
print("La calificacion final ponderada es:", calificacion_final)
