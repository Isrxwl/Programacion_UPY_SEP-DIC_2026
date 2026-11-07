#Pseudocodigo:
INPUT
Leer total_botellas  # El numero de botellas que llegaron al almacen

PROCESS
cajas_llenas <- total_botellas DIV 12  # Cantidad de cajas que se logran llenar
botellas_sobrantes <- total_botellas MOD 12  # Botellas sueltas que no alcanzan para otra caja
tarimas_llenas <- cajas_llenas DIV 20  # Cantidad de tarimas completas
cajas_sobrantes <- cajas_llenas MOD 20  # Cajas que sobran y no llenan una tarima

OUTPUT
Mostrar cajas_llenas
Mostrar botellas_sobrantes
Mostrar tarimas_llenas
Mostrar cajas_sobrantes

#Codigo Python

INPUT
total_botellas = int(input())

PROCESS
cajas_llenas = total_botellas // 12
botellas_sobrantes = total_botellas % 12
tarimas_llenas = cajas_llenas // 20
cajas_sobrantes = cajas_llenas % 20

OUTPUT
print(cajas_llenas)
print(botellas_sobrantes)
print(tarimas_llenas)
print(cajas_sobrantes)


#Traza para 1000 botellas:
cajas = 83

botellas sobrantes = 4

tarimas = 4

cajas sobrantes = 3
