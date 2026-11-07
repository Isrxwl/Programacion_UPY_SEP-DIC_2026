temp = float(input("Ingresa la temperatura en Celsius: "))

if temp <= 0:
    print("Solido (hielo)")
elif temp < 100:
    print("Liquido (agua)")
else:
    print("Gaseoso (vapor)")
