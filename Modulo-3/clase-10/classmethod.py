class Empleado:
    sueldo_base = 100.000

    def __init__(self, _name):
        self.__name = _name
        self.__color = 'Gris'
        self._b = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _name):
        self.__name = _name


    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, _name):
        self.__name = _name

    @classmethod
    def obtener_sueldo_base(cls):
        return cls.sueldo_base
    
    @classmethod
    def modificar_sueldo_base(cls, _sueldo):
        cls.sueldo_base = _sueldo


abc = Empleado("Yo")

print(abc._b)

class T(Empleado):
    def __init__(self, _name):
        super().__init__(_name)

c = T('ME')

print(c._b)