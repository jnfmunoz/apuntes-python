def tipoImpositivo():
    renta = int(input('Ingrese renta anual usuario: '))
    if renta < 10000:
        interes = "5%"
    elif renta >= 10000 and renta <= 20000:
        interes = "15%"
    elif renta > 20000 and renta <= 35000:
        interes = "20%"
    elif renta > 35000 and renta <= 60000:
        interes = "30%"
    elif renta > 60000:
        interes = "45%"
    
    print(f"El tipo impositivo que corresponde es de {interes}")

tipoImpositivo()