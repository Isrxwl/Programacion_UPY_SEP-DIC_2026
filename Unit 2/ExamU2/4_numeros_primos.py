# INPUT
n = int(input("Ingresa N: "))

# PROCESS
total_primos = 0

# 1. Ciclo externo que recorre del 2 hasta N inclusive

for numero in range(2, n + 1):
    
    # 2. Bandera booleana inicializada en True dentro del ciclo externo
    
    es_primo = True
    
    # 3. Ciclo interno que prueba los divisores del numero
    
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            # 4. Usa break al encontrar el primer divisor exacto
            
            break
            
    # 5. El if que decide si imprime va despues del ciclo interno
    
    if es_primo:
        
        # OUTPUT
        
        print(numero)
        
        # 6. Lleva el contador
        
        total_primos = total_primos + 1

# OUTPUT final
print("Total de primos:", total_primos)
