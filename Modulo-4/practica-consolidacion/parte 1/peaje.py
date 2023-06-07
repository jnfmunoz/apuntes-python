class Vehiculo():
    
    def __init__(self, _marca, _modelo, _num_ruedas) -> None:
        self.marca = _marca,
        self.modelo = _modelo,
        self.num_ruedas = _num_ruedas

class Automovil(Vehiculo):
    
    def __init__(self):

        self.automoviles = []
        
    def agregar_automovil(self):
        """ Agrega un nuevo automóvil. """
        cant_vehiculo = int(input("Cuántos vehículos desea insertar: "))
        for x in range(cant_vehiculo):
            
            print(f"Datos del automóvil: {x+1}")
            _marca = input("Ingrese marca vehiculo: ")
            _modelo = input("Ingrese modelo vehiculo: ")
            _num_ruedas = int(input("Ingrese número de ruedas: "))
            _velocidad = int(input("Ingrese velocidad(km/h) del automóvil: "))
            _cilindrada = int(input("Ingrese cilindrada(cc) del automóvil: "))

            if es_cadena_no_vacia(_marca):
                self.marca = _marca
            else:
                raise TypeError("Marca del automóvil debe ser una cadena no vacía")

            if es_cadena_no_vacia(_modelo):
                self.modelo = _modelo
            else:
                raise TypeError("Modelo del automóvil debe ser una cadena no vacía")
            
            if es_numero(_num_ruedas):
                self.num_ruedas = _num_ruedas
            else:
                raise TypeError("Número de ruedas debe ser un valor númerico")
            
            if es_numero(_num_ruedas):
                self.velocidad = _velocidad
            else:
                raise TypeError("Velocidad del automóvil debe ser un valor númerico")

            if es_numero(_cilindrada):
                self.cilindrada = _cilindrada
            else:
                raise TypeError("Cilindrada del automóvil debe ser un valor númerico")
            
            self.automoviles.append({
                "marca": self.marca,
                "modelo": self.modelo,
                "num_ruedas": self.num_ruedas,
                "velocidad": self.velocidad,
                "cilindrada": self.cilindrada,
            })
            
    def listar_automovil(self):
        """ Lista todos los automóviles registrados. """
        contador = 1
        print("Imprimiendo por pantalla los Vehículos:")
        for x in self.automoviles:
            print(f"Datos del automóvil {contador}: Marca {x['marca']}, Modelo {x['modelo']}, {x['num_ruedas']} ruedas, {x['velocidad']} Km/h, {x['cilindrada']} cc")
            contador+=1
            
def es_numero(valor):
    """ Indica si un valor es numérico o no. """
    return isinstance(valor, (int,float,complex))

def es_cadena_no_vacia(cadena):
    """ Valida que una cadena de texto no se encuentre vacía. """
    if len(cadena) > 0:
        return cadena

auto = Automovil()
auto.agregar_automovil()
auto.listar_automovil()