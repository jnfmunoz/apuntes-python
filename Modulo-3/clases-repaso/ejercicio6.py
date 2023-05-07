def calculoPeso():
    num_payasos = int(input('Ingrese cantidad de payasos vendidos: '))
    num_munecas = int(input('Ingrese cantidad de muñecas vendidas: '))

    peso_payaso = 112
    peso_muneca = 75

    peso_total = ((peso_payaso*num_payasos)+(peso_muneca*num_munecas))

    print(f'El peso total del paquete a enviar es de: {peso_total} g')

calculoPeso()