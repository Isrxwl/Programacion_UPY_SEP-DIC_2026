usuario = input("Usuario: ")
contrasena = input("Contrasena: ")

if usuario == "admin":
    if contrasena == "1234":
        print("Bienvenido")
    else:
        print("Contrasena incorrecta")
else:
    print("Usuario desconocido")
