def tipoImpositivo():
    renta = int(input('Ingrese renta anual usuario: '))
    if renta < 10000:
        print("Tienes que pagar el 5% de interés")
    elif renta >= 10000 and renta <= 20000:
        print("Tienes que pagar el 15% de interés")
    elif renta > 20000 and renta <= 35000:
        print("Tienes que pagar el 20% de interés")
    elif renta > 35000 and renta <= 60000:
        print("Tienes que pagar el 30% de interés")
    elif renta > 60000:
        print("Tienes que pagar el 45% de interés")
        
tipoImpositivo()