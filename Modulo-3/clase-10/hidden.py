class Droid:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        self.__name = name

arturo = Droid("Arturo")


print(arturo.name)

# Cree una clase llamada artefacto, agrenguele tres atributos y 
# utilice los getter and setter para acceder a ellos
class Artefacto:
    def __init__(self, nombre, autor, precio):
        self.__nombre = nombre,
        self.__autor = autor,
        self.__precio = precio

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def autor(self) -> str:
        return self.__autor
        
    @property
    def precio(self) -> str:
        return self.__precio
    
    @nombre.setter 
    def nombre(self, nombre:str) -> None:
        self.__nombre = nombre
    
    @autor.setter
    def autor(self, autor:str) -> None:
        self.__autor = autor

    @precio.setter
    def precio(self, precio:int) -> None:
        self.__precio = precio

artefacto = Artefacto("Crimen y Castigo", "Fiodor Dostoyevski", 5000)
print(artefacto.nombre, artefacto.autor, artefacto.precio)
