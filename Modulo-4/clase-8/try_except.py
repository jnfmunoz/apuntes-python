# Sintaxis try except
# while True:
#     try:
#         edad = int(input("introduce tu edad: "))
#         break
#     except ValueError:
#         print("debes introducir una edad valida")

#dividiendo
dividendo = 100
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        calculo = dividendo / edad
        print(f'el resultado es: {calculo}')
        break
    except ValueError:
        print("debes introducir una edad valida")
    except ZeroDivisionError:
        print("la edad debe ser mayor a zero")

