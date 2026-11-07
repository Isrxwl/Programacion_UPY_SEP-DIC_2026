def invertir(texto):
    if texto == "":
        return ""
    return texto[-1] + invertir(texto[:-1])

print(invertir("programacion"))

def es_palindromo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return es_palindromo(texto[1:-1])

print(es_palindromo("reconocer"))
print(es_palindromo("python"))
