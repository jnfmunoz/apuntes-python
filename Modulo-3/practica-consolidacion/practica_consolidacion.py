lista_nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
magos=[lista_nombres[0], lista_nombres[2], lista_nombres[5]]
cientificos=[lista_nombres[1], lista_nombres[3]]
otros = []

#agregamos a la lista otros los nombres de aquellas personas que no pertenecen al grupo de magos ni científicos
for x in lista_nombres:
    if x not in magos and x not in cientificos:
        otros.append(x)

def hacer_grandioso():        
    ''' modifica la lista de magos añadiendo la frase 'El gran' antes del nombre de cada mago'''
    for x in magos:
        print(f'El gran {x}')

def imprimir_nombres():
    '''Imprime el nombre de cada persona de la lista'''
    for x in lista_nombres:
        print(f'Nombre persona: {x}')

#imprimir en pantalla la lista completa de nombres antes de ser modificados
print('-----------------------------')
print('Listado de todas las personas')
for x in lista_nombres:    
    print(f'Nombre persona: {x}')

# imprimir los nombres de los magos grandiosos
print('-----------------------------')
print('Listado de los magos grandiosos')
hacer_grandioso()

#imprimir los nombres de los científicos
print('-----------------------------')
print('Listado de los científicos')
for x in cientificos:
    print(f'Nombre científico: {x}')

#imprimir los nombres restantes
print('-----------------------------')
print('Listado de los restantes')
for x in otros:
    print(f'Nombre persona: {x}')