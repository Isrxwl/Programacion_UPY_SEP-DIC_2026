peso = float(input("Ingresa el peso en kg: "))
estatura = float(input("Ingresa la estatura en m: "))

imc = peso / estatura**2

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"{round(imc, 1)} {categoria}")
