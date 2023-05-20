from itertools import combinations

def suma_cero():
    listado_numeros = []
    listado_suma_cero = []

    cantidad = int(input('ingrese cantidad de números a combinar: '))
    
    for x in range(cantidad):
        numero = int(input('ingrese numero: '))
        listado_numeros.append(numero)
        listado_combinaciones = list(combinations(listado_numeros,3))

    for x in listado_combinaciones:
        if sum(x) == 0:
            listado_suma_cero.append(x)
    
    print(listado_suma_cero)
suma_cero()