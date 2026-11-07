def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32

temperaturas = [0, 25, 37, 100]

for y in temperaturas:
    f = celsius_a_fahrenheit(y)
    print(f"{y} da {f}")
