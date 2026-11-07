def familia(codigo):
    tipo = codigo // 100
    if tipo == 2:
        return "exito"
    elif tipo == 3:
        return "redireccion"
    elif tipo == 4:
        return "error del cliente"
    elif tipo == 5:
        return "error del servidor"
    return "desconocido"

codigos = [200, 201, 301, 404, 403, 500, 503]
resumen = {"exito": 0, "redireccion": 0, "error del cliente": 0, "error del servidor": 0}

for c in codigos:
    fam = familia(c)
    print(f"Código {c}: {fam}")
    resumen[fam] += 1

print("\n--- Comprobación ---")
for fam, conteo in resumen.items():
    if conteo > 0:
        print(f"{conteo} de {fam}")
