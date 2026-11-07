# INPUT
total = float(input("Ingresa el total de la compra: "))
membresia = input("¿Tienes membresia? (si/no): ")

# PROCESS
if total > 500 and membresia == "si":
    descuento = total * 0.10
    total_a_pagar = total - descuento
    
    # OUTPUT
    print("Total a pagar con descuento:", total_a_pagar)
else:
    # OUTPUT
    print("Total a pagar sin descuento:", total)
