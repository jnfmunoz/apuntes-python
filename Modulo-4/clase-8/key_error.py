class Animal:
    def __init__(self, _name) -> None:
        self.name = _name
        self.types = {
            "gato": 1,
            "perro": 2
        }

    def test_error(self, tipo_animal):
        try:
            print(self.types[tipo_animal])
        except KeyError:
            print(f"el {tipo_animal} no existe en el zoologico")


michu = Animal("Michu")

tipo = input("adivina los animales, dime un tipo")
michu.test_error(tipo)