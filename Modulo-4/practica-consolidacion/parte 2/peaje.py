class Vehiculo():
    def __init__(self, _marca, _modelo, _num_ruedas):
        self.marca = _marca
        self.modelo = _modelo
        self.num_ruedas = _num_ruedas
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Vehiculo"

class Automovil(Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada):
        self.marca = _marca
        self.modelo = _modelo
        self.num_ruedas = _num_ruedas
        self.velocidad = _velocidad
        self.cilindrada = _cilindrada
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Automovil"

class Particular(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _numero_puestos):
        Automovil.__init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada)
        self.numero_puestos = _numero_puestos
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Particular"
    
class Carga(Automovil):
    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _peso_carga):
        Automovil.__init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada)
        self.peso_carga = _peso_carga
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Carga"

class Bicicleta(Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta):
        Vehiculo.__init__(self, _marca, _modelo, _num_ruedas)
        self.tipo_bicicleta = _tipo_bicicleta
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Bicicleta"

class Motocicleta(Bicicleta):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta, _motor, _cuadro, _nro_radios):
        Bicicleta.__init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta)
        self.motor = _motor
        self.cuadro = _cuadro
        self.nro_radios = _nro_radios
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Motocicleta"

#marca, modelo, num_ruedas, velocidad, cilindrada, num_puestos
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

print(f"Marca {particular.marca}, Modelo {particular.modelo}, {particular.num_ruedas} ruedas, {particular.velocidad} Km/h, {particular.cilindrada} cc, Puestos: {particular.numero_puestos}")
print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.num_ruedas} ruedas, {carga.velocidad} Km/h, {carga.cilindrada} cc, Carga: {carga.peso_carga} Kg")
print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.num_ruedas} ruedas, Tipo: {bicicleta.tipo_bicicleta}")
print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.num_ruedas} ruedas, Tipo: {motocicleta.tipo_bicicleta}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")

def is_instance(valor, valor2):
    if isinstance(valor, (valor2)):
        print(f"{valor} es instancia con relación a {valor2.__name__}: {True}")
    else:
        print(f"{valor} es instancia con relación a {valor2.__name__}: {False}")

is_instance(motocicleta, Vehiculo) #true
is_instance(motocicleta, Automovil) #false
is_instance(motocicleta, Particular) #false
is_instance(motocicleta, Carga) #false
is_instance(motocicleta, Bicicleta) #true
is_instance(motocicleta, Motocicleta) #true