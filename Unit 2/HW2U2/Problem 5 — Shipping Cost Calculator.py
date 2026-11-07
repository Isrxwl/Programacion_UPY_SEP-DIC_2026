costo_total = 0.0
entrada_peso = ""

while entrada_peso != "exit":
    # INPUT
    entrada_peso = input("Enter weight (kg) or 'exit': ")
    
    # PROCESS
    if entrada_peso != "exit":
        peso = float(entrada_peso)
        
        distancia_str = input("Enter distance (km): ")
        distancia = float(distancia_str)
        
        # Evaluamos primero la distancia y luego el peso (límite de 5kg)
        if distancia <= 100:
            if peso <= 5:
                costo_envio = 50.00
            else:
                costo_envio = 80.00
        else:
            if peso <= 5:
                costo_envio = 120.00
            else:
                costo_envio = 200.00
                
        costo_total = costo_total + costo_envio
        
        # OUTPUT
        print(f"Shipping cost: ${costo_envio:.2f} MXN")

# OUTPUT (Imprime el total acumulado al romper el ciclo)
if costo_total > 0:
    print(f"Total: ${costo_total:.2f} MXN")
