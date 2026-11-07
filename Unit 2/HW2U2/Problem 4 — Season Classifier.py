entrada = ""

while entrada != "exit":
    # INPUT
    entrada = input("Enter month number (1-12) or 'exit': ")
    
    # PROCESS
    if entrada != "exit":
        mes = int(entrada)
        
        # OUTPUT
        if mes == 12 or mes == 1 or mes == 2:
            print("Winter")
        elif mes == 3 or mes == 4 or mes == 5:
            print("Spring")
        elif mes == 6 or mes == 7 or mes == 8:
            print("Summer")
        elif mes == 9 or mes == 10 or mes == 11:
            print("Fall")
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
