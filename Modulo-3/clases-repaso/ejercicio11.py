def tributar():
    edad = int(input("Ingrese edad usuario: "))
    ingreso_mensual = int(input("Ingreso mensual: "))

    if edad > 16 and ingreso_mensual >= 1000:
        print("Usuario debe tributar")
    else:
        print("Usuario no tributa")

tributar()