import csv

class Vehiculo():

    def __init__(self, _marca, _modelo, _num_ruedas):

        if es_cadena_no_vacia(_marca):
            self.marca = _marca
        else:
            raise TypeError("marca de vehículo debe ser una cadena de caracteres no vacía")
        
        if es_cadena_no_vacia(_modelo):
            self.modelo = _modelo
        else:
            raise TypeError("modelo de vehículo debe ser una cadena de caracteres no vacía")
        
        if es_numero(_num_ruedas):
            self.num_ruedas = _num_ruedas
        else:
            raise TypeError("número de ruedas de vehículo debe ser un valor númerico")
        
    def guardar(file_name, Vehiculo):

        try:
            file = open(file_name, "a")
            datos = [(Vehiculo.__class__, Vehiculo.__dict__)]
            csv_file = csv.writer(file, lineterminator='\n')
            csv_file.writerows(datos)
            file.close()

        except csv.Error as e:
            print(f"Error: {e}")
    
    def recuperar(file_name):
        
        vehiculos = []

        try:
            file = open(file_name, "r")
            file_csv = csv.reader(file)
            for vehiculo in file_csv:
                vehiculos.append(vehiculo)
            file.close()

        except csv.Error as e:
            print(f"Error: {e}")
            
        else:
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
        
        Vehiculo.__init__(self, _marca, _modelo, _num_ruedas)
        
        if es_numero(_velocidad):
            self.velocidad = _velocidad
        else:
            raise TypeError("velocidad del vehículo debe ser un valor númerico")

        if es_numero(_cilindrada):
            self.cilindrada = _cilindrada
        else:
            raise TypeError("cilindrada del vehículo debe ser un valor númerico")
        
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Automovil"

class Particular(Automovil):

    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _numero_puestos):
        Automovil.__init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada)

        if es_numero(_numero_puestos):
            self.numero_puestos = _numero_puestos
        else:
            raise TypeError("número de puestos del vehículo debe ser un valor númerico")
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Particular"
    
class Carga(Automovil):

    def __init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada, _peso_carga):
        Automovil.__init__(self, _marca, _modelo, _num_ruedas, _velocidad, _cilindrada)
       
        if es_numero(_peso_carga):
            self.peso_carga = _peso_carga
        else:
            raise TypeError("número de puestos del vehículo debe ser un valor númerico") 
        
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Carga"

class Bicicleta(Vehiculo):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta):
        Vehiculo.__init__(self, _marca, _modelo, _num_ruedas)
        
        if es_cadena_no_vacia(_tipo_bicicleta):
            self.tipo_bicicleta = _tipo_bicicleta
        else:
            raise TypeError("Tipo de bicicleta debe ser una cadena de caracteres no vacía")
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Bicicleta"

class Motocicleta(Bicicleta):
    def __init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta, _motor, _cuadro, _nro_radios):
        Bicicleta.__init__(self, _marca, _modelo, _num_ruedas, _tipo_bicicleta)
        
        if es_cadena_no_vacia(_motor):
            self.motor = _motor
        else:
            raise TypeError("Motor de la motocicleta debe ser una cadena de caracteres no vacía")
        
        if es_cadena_no_vacia(_cuadro):
            self.motor = _cuadro
        else:
            raise TypeError("Cuadro de motocicleta debe ser una cadena de caracteres no vacía")
        
        if es_numero(_nro_radios):
            self.nro_radios = _nro_radios
        else:
            raise TypeError("Nro de radios debe ser un valor numérico")
    
    def __repr__(self) -> str:
        """ Devuelve por defecto el nombre de la clase y la dirección del objeto. """
        return "Motocicleta"

def es_cadena_no_vacia(cadena):
    """ Valida si una cadena de texto se encuentra vacía o no. """
    if len(cadena) > 0:
        return cadena

def es_numero(valor):
    """ Indica si un valor es númerico o no. """
    return isinstance(valor, (int, float, complex))