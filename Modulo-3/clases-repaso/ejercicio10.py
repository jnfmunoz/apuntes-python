def dividir():
    dividendo = int(input("Ingrese dividendo: "))
    divisor = int(input("Ingrese divisor: "))
    
    try:
        resultado = dividendo/divisor 
        print(f"El resultado de la división entre {dividendo} y {divisor} es: ", resultado)
        return resultado

    except ZeroDivisionError:
        raise ZeroDivisionError("El divisor no puede ser 0")
dividir()