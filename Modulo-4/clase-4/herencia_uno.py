class Padre: 
    def __init__(self, _name_padre, _rut_padre):
        self.name = _name_padre
        self.rut_padre = _rut_padre
        self.sueldo = 0

    def pintar(self):
        print("estoy pintando")

class Hijo(Padre):
    def __init__(self, _name_hijo, _rut_hijo, _color_ojos):
        Padre.__init__(self, _name_hijo, _rut_hijo)
        self.color_cojor = _color_ojos

    def lijar(self):
        print("estoy lijando")
    
richar = Padre("Richar","1")
richard = Hijo("Richard Lujano","2", "Marron")

print(richar.name, richar.sueldo)
print(richard.name, richard.sueldo)

richar.pintar()
richard.pintar()
richard.lijar()
