numeros = [4, -2, 7, -5, 1]
suma = 0

for num in numeros:
    if num < 0:
        continue
    suma = suma + num

print("Suma de positivos:", suma)
