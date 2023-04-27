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