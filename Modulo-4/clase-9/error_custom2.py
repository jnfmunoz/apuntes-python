class NoPuedeEscribirDosException(Exception):
    def __init__(self, value):
        self.value = value
try:
    number = int(input('introduce un numero: '))
    if number == 2:
        raise NoPuedeEscribirDosException("Introdujo un numero 2 y este no es valido")
    else:
        print("numero introducido correctamente")
except Exception as error:
    print(type(error))
    print(error.args)