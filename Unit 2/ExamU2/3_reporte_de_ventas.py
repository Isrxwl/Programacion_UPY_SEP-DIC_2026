# PROCESS (Inicialización)
total_acumulado = 0
contador_validas = 0

# INPUT y PROCESS
for dia in range(7):
    venta = float(input("Ingresa la venta del dia: "))
    
    # Descarta las ventas negativas
    if venta < 0:
        continue
        
    # Acumula y cuenta solo las válidas
    total_acumulado = total_acumulado + venta
    contador_validas = contador_validas + 1

# OUTPUT
if contador_validas > 0:
    promedio = total_acumulado / contador_validas
    print("Ventas validas reportadas:", contador_validas)
    print("Total acumulado:", total_acumulado)
    print("Promedio de ventas:", promedio)
else:
    print("Sin datos validos")
