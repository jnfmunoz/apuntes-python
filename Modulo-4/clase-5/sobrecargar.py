class Persona:
    def __init__(self, _name):
        self.name = _name
    
    def llamar(self, _medio):
        print(f"Te estoy llamando con {_medio}")

juan = Persona("Juan")
juan.llamar("Telefono")