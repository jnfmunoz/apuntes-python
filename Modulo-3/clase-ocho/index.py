class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type


gato = Animal("Angora", "Persa")
print(gato.type)
gato.type = "Grandanes"
print(gato.type)


class Droid: 
    def __init__(self, name):
        self.hidden_name = name
    
    @property
    def name(self) -> str:
        return self.hidden_name

    @name.setter
    def name(self, name: str) -> None:
        self.hidden_name = name
    
android = Droid("arthur")

print(android.name)
android.name = "Critripo"
print(android.name)

android.hidden_name = "Rojo"
print(android.hidden_name)
print(android.name)

print("\n ******************************** \n")

class CalculatedValue:
    def __init__(self, _name, _height):
        self.name = _name
        self.height = _height

    @property
    def get_calculate_value(self) -> float:
        return 0.35 * self.height
    
valuex= CalculatedValue("ratio", 10)

print(f'El {valuex.name} es: {valuex.get_calculate_value}')

print("\n ******************************** \n")

class Dog:
    obeys_owner = True

    def __init__(self, _name):
        self.name = _name
    
dog_one = Dog("Robin")
dog_two = Dog("Malta")
dog_three = Dog("Luz")

print(f'{dog_one.name} obede a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obede a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obede a su dueño {dog_three.obeys_owner}')


print("\n ******************************** \n")

dog_one.obeys_owner = True
#dog_two.obeys_owner = False
print(f'{dog_one.name} obede a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obede a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obede a su dueño {dog_three.obeys_owner}')

print("\n ******************************** \n")

Dog.obeys_owner = False
print(f'{dog_one.name} obede a su dueño {dog_one.obeys_owner}')
print(f'{dog_two.name} obede a su dueño {dog_two.obeys_owner}')
print(f'{dog_three.name} obede a su dueño {dog_three.obeys_owner}')
