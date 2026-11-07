# INPUT
verbo = input("Ingrese verbo: ")

# PROCESS
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Sacamos la raíz (todo menos las últimas 2 letras) y la terminación (las últimas 2)
raiz = verbo[:-2]
terminacion = verbo[-2:]

# Buscamos la lista de terminaciones que le toca en el diccionario
terminaciones_verbo = terminaciones[terminacion]

# OUTPUT
# Recorremos la lista usando el índice para hacer match entre el pronombre y la terminación
for i in range(len(pronombres)):
    print(pronombres[i] + " " + raiz + terminaciones_verbo[i])
