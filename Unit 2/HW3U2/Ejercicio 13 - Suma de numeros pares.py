n = int(input("Ingresa N: "))
total = 0

for i in range(2, n + 1, 2):
    total = total + i

print("Suma de pares:", total)
