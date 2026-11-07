contador_llamadas = 0

def fib(n):
    global contador_llamadas
    contador_llamadas += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(10):
    print(fib(i), end=" ")
print() 

contador_llamadas = 0
fib(10)
print("Veces que se llamó la función para fib(10):", contador_llamadas)
