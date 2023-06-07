#creando una clase
class Transporte:
    pass # palabra reservada para declarar una clase vacía

#instanciando una clase y crear un objeto
transporte1 = Transporte() #instanciar-> llamar clase
transporte3 = Transporte()

class BuzzLightYear():
    pass

bozz1 = BuzzLightYear()
bozz2 = BuzzLightYear()

print(type(transporte1))
print(type(bozz1))

class Droid:
    def __init__(self):
        self.power_on = False

    def switch_on(self):
        print("Hola soy un droid, y estoy a tu orden")
        self.power_on = True
    
    def switch_off(self):
        print("Adios, enciendeme, cuando me necesites")
        self.power_on = False

k8_arthur = Droid() #Instanciando un objeto
k8_tripio = Droid()

k8_arthur.switch_on()
print("Power on Arthur: ", k8_arthur.power_on)
k8_tripio.switch_off()
print("Power on tripio: ", k8_tripio.power_on)
k8_arthur.switch_off()
print(k8_arthur.power_on)

class Vehicle():
    def __init__(self, type, model):
        self.type_vehicle = type
        self.model_vehicle = model

sedan = Vehicle('Sedan', 'Aveo')
print(sedan.type_vehicle, sedan.model_vehicle)
pickup = Vehicle('Pickup', 'Ranger')
print(pickup.type_vehicle, pickup.model_vehicle)