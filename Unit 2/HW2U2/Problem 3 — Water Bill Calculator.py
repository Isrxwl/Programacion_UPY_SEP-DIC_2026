total_acumulado = 0.0
entrada = ""

while entrada != "exit":
    # INPUT
    entrada = input("Enter m3 consumed or 'exit': ")
    
    # PROCESS
    if entrada != "exit":
        m3 = float(entrada)
        
        # Calculamos la tarifa multiplicando el total por el precio de su nivel
        if m3 <= 10:
            cargo_mes = m3 * 8.00
        elif m3 <= 20:
            cargo_mes = m3 * 12.00
        else:
            cargo_mes = m3 * 18.00
            
        total_acumulado = total_acumulado + cargo_mes
        
        # OUTPUT
        print(f"Month charge: ${cargo_mes:.2f} MXN")

# OUTPUT (Se ejecuta al salir del bucle while)
if total_acumulado > 0:
    print(f"Total: ${total_acumulado:.2f} MXN")
