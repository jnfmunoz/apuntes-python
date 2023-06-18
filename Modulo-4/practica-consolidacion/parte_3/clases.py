import csv

class Vehiculo():
    def __init__(self, _marca, _modelo, _num_ruedas):
        self.marca = _marca
        self.modelo = _modelo
        self.num_ruedas = _num_ruedas
    
    def guardar(file_name, Vehiculo):
        file = open(file_name, "a")
        datos = [(Vehiculo.__class__, Vehiculo.__dict__)]
        csv_file = csv.writer(file, lineterminator='\n')
        csv_file.writerows(datos)
        file.close()
    
    
    def recuperar(file_name):
        vehiculos = []
        file = open(file_name, "r")
        file_csv = csv.reader(file)
        for vehiculo in file_csv:
            vehiculos.append(vehiculo)
        file.close()
        return vehiculos
    
    def imprimir_por_clase(vehiculos):
        tipos = ["Particular", "Carga", "Bicicleta", "Motocicleta"]

        for tipo in tipos:
            print(f"\nLista de Vehículos {tipo}: ")
            for vehiculo in vehiculos:
                class_str = vehiculo[0].split("'")[1].rsplit('.', 1)[1]
                if class_str == tipo:
                    print(vehiculo[1])    

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