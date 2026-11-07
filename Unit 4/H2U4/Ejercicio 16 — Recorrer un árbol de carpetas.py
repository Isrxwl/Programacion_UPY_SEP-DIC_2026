arbol = {
    "nombre": "proyecto",
    "hijos": [
        {"nombre": "main.py", "hijos": []},
        {
            "nombre": "utils",
            "hijos": [
                {"nombre": "texto.py", "hijos": []},
                {"nombre": "numeros.py", "hijos": []}
            ]
        },
        {"nombre": "README.md", "hijos": []}
    ]
}

def listar(nodo, nivel=0):
    print("  " * nivel + nodo["nombre"])
    for hijo in nodo["hijos"]:
        listar(hijo, nivel + 1)

listar(arbol)
