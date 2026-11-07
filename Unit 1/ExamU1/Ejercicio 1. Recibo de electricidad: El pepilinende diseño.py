#Pseudocodigo:
INPUT
Leer kwh
Leer price

PROCESS
subtotal <- kwh * price
subtotal_con_cuota <- subtotal + 85
iva <- subtotal_con_cuota * 0.16
total <- subtotal_con_cuota + iva

OUTPUT
Mostrar total

#Codigo Python:
INPUT
kwh = float(input())
price = float(input())

PROCESS
subtotal = kwh * price
subtotal_con_cuota = subtotal + 85
iva = subtotal_con_cuota * 0.16
total = subtotal_con_cuota + iva

OUTPUT
print(total)
