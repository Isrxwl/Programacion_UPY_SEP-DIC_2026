def suma_rec(n):
    if n == 1:
        return 1
    return n + suma_rec(n - 1)

def suma_iter(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Con 100 (rec):", suma_rec(100))
print("Con 100 (iter):", suma_iter(100))

try:
    suma_rec(5000)
except RecursionError:
    print("Error: Se alcanzó el límite de la pila de recursión")

print("Con 5000 (iter):", suma_iter(5000))
