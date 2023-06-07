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
        result = dividendo / edad
        break
    except ValueError as error:
        print("debe de colocar una edad valida")
        print(type(error))
        print(error.args)
        print(error)
    except ZeroDivisionError as error:
        print(type(error))
        print(error.args)
        print(error)
