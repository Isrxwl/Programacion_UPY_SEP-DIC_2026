entrada_peso = ""

while entrada_peso != "exit":
    # INPUT
    entrada_peso = input("Enter weight (kg) or 'exit': ")
    
    # PROCESS
    if entrada_peso != "exit":
        peso = float(entrada_peso)
        
        # Pedimos la altura solo si no se escribió exit
        altura_str = input("Enter height (m): ")
        altura = float(altura_str)
        
        imc = peso / (altura * altura)
        
        # OUTPUT
        if imc < 18.5:
            print(f"weight = {peso:g}, height = {altura} BMI: {imc:.2f} — Underweight")
        elif imc <= 24.9:
            print(f"weight = {peso:g}, height = {altura} BMI: {imc:.2f} — Normal")
        elif imc <= 29.9:
            print(f"weight = {peso:g}, height = {altura} BMI: {imc:.2f} — Overweight")
        else:
            print(f"weight = {peso:g}, height = {altura} BMI: {imc:.2f} — Obese")
