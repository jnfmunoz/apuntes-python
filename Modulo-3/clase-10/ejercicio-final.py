class Cuenta:

    saldo = 0
    movimientos = 0 
    n_movimientos = 0

    def __init__(self, nombre, rut, n_cuenta, tipo_cuenta):
        self.__nombre = nombre,
        self.__rut = rut,
        self.__n_cuenta = n_cuenta,
        self.__tipo_cuenta = tipo_cuenta,

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def rut(self) -> str:
        return self.__rut
    
    @property
    def n_cuenta(self) -> int:
        return self.__n_cuenta
    
    @property
    def tipo_cuenta(self) -> str:
        return self.__tipo_cuenta

    @nombre.setter
    def nombre(self, nombre:str) -> None:
        self.__nombre = nombre

    @rut.setter
    def rut(self, _rut:str) -> None:
        self.__rut = _rut

    @n_cuenta.setter
    def n_cuenta(self, n_cuenta) -> None:
        self.__n_cuenta = n_cuenta        

    @tipo_cuenta.setter
    def tipo_cuenta(self, tipo_cuenta) -> None:
        self.__tipo_cuenta = tipo_cuenta

    #metodo para abonar saldo a la cuenta bancaria
    # @staticmethod
    @classmethod
    def abono_saldo(monto):
        saldo =+ monto
        return saldo
    
    #metodo para realizar cargo a la cuenta bancaria
    #@staticmethod
    @classmethod
    def cargo_saldo(monto):
        saldo =- monto
        return saldo

def mostrar_menu(nombre, opciones):  # incorporamos el parámetro para mostrar el nombre del menú
    print(f'{nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(nombre, opciones, opcion_salida):  # incorporamos el parámetro para mostrar el nombre del menú
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Crear cuenta bancaria', funcion1),
        '2': ('Abono-Cargo de cuenta >', submenu),  # la acción es una llamada a submenu que genera un nuevo menú
        '3': ('Consulta de saldo y movimientos', funcion3),
        '4': ('Salir', salir)
    }

    generar_menu('Menú principal', opciones, '4')  # indicamos el nombre del menú


def submenu():
    opciones = {
        'a': ('Realizar abono de cuenta', funcionA),
        'b': ('Realizar cargo de cuenta', funcionB),
        'c': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'c')  # indicamos el nombre del submenú


# A partir de aquí creamos las funciones que ejecutan las acciones de los menús
def funcion1():

    nombre = input("Ingrese su nombre cliente: ")
    rut = input("Ingrese su rut: ")
    n_cuenta = int(input("Ingrese n° cuenta: "))
    tipo_cuenta = input("Ingrese tipo cuenta: ")
    cuenta = Cuenta(nombre, rut, n_cuenta, tipo_cuenta)
    print('Cuenta registrada con éxito')
    print('Nombre de cliente: ', nombre)
    print('Rut cliente: ', rut)
    print('N° de cuenta: ',  n_cuenta)
    print('Tipo de cuenta: ', tipo_cuenta)
    print('Saldo inicial: ', cuenta.saldo)

def funcion2():
    print('Has elegido la opción 2')


def funcion3():
    print('Has elegido la opción 3')


def funcionA():
    monto= int(input("Ingrese monto a abonar: "))
    saldo_abonado = Cuenta.abono_saldo(monto)
    print('Éxito, saldo abonado')
    print('Nuevo Saldo: ',saldo_abonado)


def funcionB():
    monto= int(input("Ingrese monto para cargo: "))
    saldo_restante = Cuenta.cargo_saldo(monto)
    print('Éxito, saldo cargado')
    print('Nuevo Saldo: ',saldo_restante)

def salir():
    print('Saliendo')

if __name__ == '__main__':
    menu_principal() # iniciamos el programa mostrando el menú principal
