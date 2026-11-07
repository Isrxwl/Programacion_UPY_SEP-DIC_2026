palabra = input("Ingresa una palabra: ")
contador_vocales = 0

for letra in palabra:
    if letra.lower() in "aeiou":
        contador_vocales = contador_vocales + 1

print(contador_vocales, "vocales")
