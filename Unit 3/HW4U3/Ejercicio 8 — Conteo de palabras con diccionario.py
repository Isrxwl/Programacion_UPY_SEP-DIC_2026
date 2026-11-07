frase = "the cat and the dog and the bird"
conteo = {}

for palabra in frase.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
    
print(conteo)
