class Cuenta:
    def __init__(self, nombre, rut, n_cuenta, tipo_cuenta):
        self._nombre,
        self._rut,
        self._n_cuenta,
        self._tipo_cuenta,


class Movimientos(Cuenta):
    def __init__(self, n_movimiento, n_cuenta ,tipo_movimiento, 
                 fecha_movimiento, monto_movimiento, saldo):
        self.__n_movimiento,
        self.__tipo_movimiento,
        self.__fecha_movimiento,
        self.__monto_movimiento,
        self.__saldo,

    @property
    def n_movimiento(self):
        return self.__n_movimiento
    
    @property
    def tipo_movimiento(self):
        return self.__tipo_movimiento

    @property
    def fecha_movimiento(self):
        return self.__fecha_movimiento
    
    @property
    def monto_movimiento(self):
        return self.__monto_movimiento
    
    @property
    def saldo(self):
        return self.__saldo
    
    @n_movimiento.setter
    def n_movimiento(self, _n_movimiento:str) -> None:
        self._n_movimiento
    
    @tipo_movimiento.setter
    def tipo_movimiento(self, _tipo_movimiento:str) -> None:
        self._tipo_movimiento
    
    @fecha_movimiento.setter
    def fecha_movimiento(self, _fecha_movimiento:str) -> None:
        self._fecha_movimiento

    @monto_movimiento.setter
    def monto_movimiento(self, _monto_movimiento:str) -> None:
        self._monto_movimiento

    @saldo.setter
    def saldo(self, _saldo:str) -> None:
        self._saldo
