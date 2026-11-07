
suma = 0.0
contador = 0
entrada = ""

while entrada != "done":
    # INPUT
    entrada = input("Enter a grade or 'done': ")
    
    # PROCESS
    if entrada != "done":
        calificacion = float(entrada)
        suma = suma + calificacion
        contador = contador + 1

# OUTPUT
if contador == 0:
    print("No grades entered. Please enter at least one grade.")
else:
    promedio = suma / contador
    
    if promedio >= 7.0:
        # El .2f asegura que se impriman dos decimales como en el ejemplo
        print(f"Average: {promedio:.2f} — Passed")
    else:
        print(f"Average: {promedio:.2f} — Failed")

