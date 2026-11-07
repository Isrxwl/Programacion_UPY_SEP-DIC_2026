# PPP (Pseudocódigo)
# INPUT
# 1. Leer el precio original del producto
# PROCESS
# 2. Calcular el descuento multiplicando el precio original por 0.15 (15%)
# 3. Calcular el precio con descuento restando el descuento al precio original
# 4. Calcular el IVA multiplicando el precio con descuento por 0.16 (16%)
# 5. Calcular el precio final sumando el IVA al precio con descuento
# OUTPUT
# 6. Mostrar el precio final del producto

# PPP enfocado a Python (Código funcional)

# INPUT
precio = float(input("Ingresa el precio del producto: "))

# PROCESS
# Se aplica el 15% de descuento
descuento = precio * 0.15
precio_con_descuento = precio - descuento

# Se aplica el 16% de IVA sobre el precio ya descontado
iva = precio_con_descuento * 0.16
precio_final = precio_con_descuento + iva

# OUTPUT
print("El precio final a pagar es:", precio_final)
