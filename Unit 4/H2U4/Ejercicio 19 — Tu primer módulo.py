with open("geometria.py", "w") as f:
    f.write("PI = 3.1416\n\n")
    f.write("def area_circulo(r):\n")
    f.write("    return PI * r * r\n")

import geometria

print("PI:", geometria.PI)
print("Area de radio 2:", geometria.area_circulo(2))
