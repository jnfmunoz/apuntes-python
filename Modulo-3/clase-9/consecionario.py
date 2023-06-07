class Motocicleta:
    is_new = True
    motor = False

    def __init__(self, _color, _matricula, _combustible_litros, _numero_ruedas, 
                 _marca, _modelo, _fecha_fabricacion, _velocidad_punta, _peso, _maximo_combustible,):
        self.color = _color
        self.matricula = _matricula
        self.combustible_litros = _combustible_litros
        self.numero_ruedas = _numero_ruedas
        self.marca = _marca
        self.modelo = _modelo 
        self.fecha_fabricacion = _fecha_fabricacion
        self.velocidad_punta = _velocidad_punta
        self.peso = _peso
        self.maximo_combustible = _maximo_combustible

    # if self.variable == False:  ==== if not self.variable:
    # if self.variable == True:   ==== if self.variable:

    def arrancar(self):
        # if self.motor == True:        
        #   print("El motor ha arrancado")
        # if self.motor == False:
        #   print("El motor ya estaba en marcha")

        # if self.motor:        
        #   print("El motor ha arrancado")
        # if not self.motor:
        #   print("El motor ya estaba en marcha")

        if not self.motor:
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba en marcha")

    def detener(self):
        if not self.motor:
            print("El motor ya estaba detenido")
        else:
            print("El motor se ha apagado")
    
    def consultar_precio(self):
        print(f'El precio de la motocicleta {self.marca} {self.modelo} es de {self.precio}$')

    def comprobar_combustible(self):
        print(f'El reporte del la moto {self.marca} {self.modelo} es:')
        print(f'La capacidad maxima de combustible de esta moto es {self.maximo_combustible}')
        print(f'El combustible actual es {self.combustible_litros}')
        print(f'Para llenar el estanque faltan: {self.maximo_combustible - self.combustible_litros}')

    def colocar_combustible(self):
        while True:
            litros_colocar = float(input('ingrese la cantidad de listros a repostar'))
            if litros_colocar + self.combustible_litros <= self.maximo_combustible:
                print("Repostaje exitoso")
                break
            else:
                print('La cantidad de combustible a colocar, supera el maximo, \n intente con una cifra menos')


            



#moto1 = Motocicleta("Negro", "XX22", 10, 2, "Kawasaki", "Ninja", "03/10/2023", 200, 120)

moto_2 = Motocicleta(_matricula="XXX-126", _combustible_litros=10, _color="Negra", _marca="ZONTES", _modelo="V-310", 
                     _numero_ruedas=2, _peso=150, _fecha_fabricacion="19/09/2023", _velocidad_punta=150, _maximo_combustible = 25)

# moto1.arrancar()
# moto1.detener()
# moto1.precio = 9000
# print(f'El precio de la motocicleta {moto1.marca} {moto1.modelo} es de {moto1.precio}$')
# moto1.consultar_precio()

moto_2.comprobar_combustible()