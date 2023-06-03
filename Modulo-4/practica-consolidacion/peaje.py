class Vehiculo():
    
    def __init__(self, _marca, _modelo, _num_ruedas):
        self.marca = _marca,
        self.modelo = _modelo,
        self.num_ruedas = _num_ruedas

class Automovil(Vehiculo):
    
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada):
         Vehiculo.__init__(self, _marca, _modelo, _num_ruedas)
         self.velocidad = _velocidad
         self.cilindrada = _cilindrada

    #def registrar_automovil(self):



#francesco = Automovil("chevrolet","aveo",4, 220, 23)
#print(francesco.marca,francesco.modelo)