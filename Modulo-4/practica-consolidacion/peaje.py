class Vehiculo():
    
    def __init__(self, _marca, _modelo, _num_ruedas) -> None:
        self.marca = _marca,
        self.modelo = _modelo,
        self.num_ruedas = _num_ruedas

class Automovil(Vehiculo):
    
    def __init__(self):

        self.automoviles = []

    def agregar_automovil(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada):

        Vehiculo.__init__(self, _marca, _modelo, _num_ruedas)
        self.velocidad = _velocidad,
        self.cilindrada = _cilindrada
        self.automoviles.append({
            "marca": _marca,
            "modelo": _modelo,
            "num_ruedas": _num_ruedas,
            "velocidad": _velocidad,
            "cilindrada": _cilindrada,
        })

    def listar_automovil(self):
        for x in self.automoviles:
            print("Marca: ", x['marca'], "Modelo: " ,x['modelo'], "Número de ruedas: ", x['num_ruedas'], "Velocidad(km/h): " ,x['velocidad'], x['cilindrada'])

Angostura = Automovil()
Angostura.agregar_automovil("chevrolet","aveo",4, 220, "1600cc")
Angostura.agregar_automovil("Nissan","V16",4, 300, "1400cc")
Angostura.listar_automovil()
#print(Angostura.automoviles)
