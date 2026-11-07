#Parte A: 
7 // 2 -> Tipo: int | Valor: 3 
7 / 2 -> Tipo: float | Valor: 3.5 
"7" + "2" -> Tipo: str | Valor: "72"   
7 > 2 and 2 > 7 -> Tipo: bool | Valor: False

#Parte B
b.1) Después de las dos primeras líneas, las variables price y qty son de tipo str (texto) porque input() siempre guarda texto. 
Los dos errores son: 
1) Intentar multiplicar dos textos en la línea 3, lo cual da error matemático. 
2) En la línea 4 se intenta concatenar un texto ("Total: ") con una variable que debería ser un número, lo cual choca si no se le hace casting a string.  
b.2) Código corregido:   

INPUT
price = float(input("Price: "))
qty = int(input("Quantity: "))

PROCESS
total = price * qty

OUTPUT
print("Total: " + str(total))

#Parte c
Línea de salida: print(f"Total: {total:.2f}")
Resultado esperado: Total: 76.50
