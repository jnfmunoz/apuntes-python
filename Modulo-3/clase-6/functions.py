def saludar(name):
    print(f'Hola {name} !!!')

def saludar_dos(first_name, last_name):
    print(f'Hola {first_name}, {last_name}!!!')

def multiplcar_texto(texto, multiplier = 2):
    print(texto * multiplier)

def varieltal(param1, param2, *others):
    print(param1)
    print(param2)
    print(others)

def varietal_dos(param1, **others):
    print(param1)
    print(others)

saludar('Rodrigo')
saludar('Richar')
saludar_dos(last_name = 'Lujano', first_name = 'Richar')
multiplcar_texto("V", 5)

multiplcar_texto("X")

print("\n---------------------\n")
varieltal("1A", "2B", 0, "XX", [0, 1])

print("\n---------------------\n")
varietal_dos("1A", id = 0, name ='Carlos')