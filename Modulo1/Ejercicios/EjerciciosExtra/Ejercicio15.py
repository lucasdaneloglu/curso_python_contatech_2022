intents = 0
right_credentials = False
while not right_credentials and intents < 3:
    intents += 1
    user = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")
    if user == "admin" and password == "admin":
        right_credentials = True
        print("Ha ingresado correctamente")
if not right_credentials:
    print("Se ha bloqueado la cuenta.")
