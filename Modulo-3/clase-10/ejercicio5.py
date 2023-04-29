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
    @staticmethod
    def abono_saldo(monto):
        saldo =+ monto
        return saldo
    
    #metodo para realizar cargo a la cuenta bancaria
    @staticmethod
    def cargo_saldo(monto):
        saldo =- monto
        return saldo
    
    #metodo para revisar estado de cuenta bancaria
    #@staticmethod
    # def estado_cuenta()

nombre = input("Ingrese su nombre cliente: ")
rut = input("Ingrese su rut: ")
n_cuenta = int(input("Ingrese n° cuenta: "))
tipo_cuenta = input("Ingrese tipo cuenta: ")
cuenta = Cuenta(nombre, rut, n_cuenta, tipo_cuenta)
print('Cuenta registrada con éxito')
print(cuenta.nombre, cuenta.rut, cuenta.n_cuenta, cuenta.tipo_cuenta, cuenta.saldo)

saldo_abonado = Cuenta.abono_saldo(2000)
print(saldo_abonado)

saldo_restante = Cuenta.cargo_saldo(2000)
print(saldo_restante)