a = int(input("Desde: "))
b = int(input("Hasta: "))

for n in range(a, b + 1):
    if n % 7 == 0:
        print("Primer multiplo de 7:", n)
        break
