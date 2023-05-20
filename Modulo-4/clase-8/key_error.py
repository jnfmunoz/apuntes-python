class Animales:
    def __init__(self, _name):
        self.name = _name
        self.types = {
            "gato":1,
            "perro":2
        }
    
    def test_errors(self):  
        try:
            print(self.types["pajaro"])
        except KeyError:
            print("el pajaro no existe en el zoologico")
    
michu = Animales("Michu")