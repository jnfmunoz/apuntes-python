def capitalAhorrado():
    cantidad = float(input("Ingrese cantidad de dinero a invertir($): "))
    interes = float(input("Ingrese porcentaje de interés: "))
    anios = float(input("Ingrese cantidad de años a invertir: "))

    capital = ((interes/100)*cantidad)*anios

    print(f"El capital a obtener de la inversión es de $ {capital} pesos")

capitalAhorrado()