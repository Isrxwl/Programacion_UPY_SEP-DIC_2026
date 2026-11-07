import csv

with open("empleados.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nombre", "sueldo"])
    w.writerow(["Ana", 12000])
    w.writerow(["Luis", 9500])
    w.writerow(["Mia", 15000])

total = 0
with open("empleados.csv", "r") as f:
    for fila in csv.DictReader(f):
        total = total + int(fila["sueldo"])
        
print("Total:", total)
