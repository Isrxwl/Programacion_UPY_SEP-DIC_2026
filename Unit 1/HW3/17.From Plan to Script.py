# PPP (Pseudocódigo)
# 1. Leer el precio del boleto (ticket_price)
# 2. Leer el número de boletos (num_tickets)
# 3. Calcular total <- ticket_price * num_tickets
# 4. Mostrar el total calculado

# PPP enfocado a Python (Código funcional simulando el script "tickets.py")
ticket_price = float(input("Ingresa el precio del boleto: "))
num_tickets = int(input("Ingresa la cantidad de boletos: "))

total = ticket_price * num_tickets
print("El total a pagar es:", total)

# Diferencia entre la Shell (interactiva) y un script guardado:
# La Shell ejecuta las instrucciones una por una al instante (ideal para pruebas rápidas), pero se borra al cerrarla. 
# En cambio, un script guardado almacena todo el código junto, permitiendo corregir errores, guardarlo para el futuro y ejecutarlo completo de una sola vez.
