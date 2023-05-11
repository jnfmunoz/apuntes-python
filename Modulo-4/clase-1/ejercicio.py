def menus():
    peso = int(input('Ingrese peso(kg) de la persona: '))

    carbohidratos = {
            'fruta':'manzana',
            'legumbre':'lentejas',
            'verdura':'maíz',
            'alimento dulce':'mermelada',
            'bocadillo':'galletas saladas',
    }
    proteinas = {
            'carne':'carne de vaca',
            'pescados y maricos':'atún',
            'lacteos':'leche de vaca',
            'huevos':'huevos de gallina',
    }
    fibras = {
            'vegetales':'Guisantes verdes hervidos',
            'cereales':'arroz integral cocido',
            'granos':'avena',
    }

    if peso >= 60 and peso < 70:
        for x in carbohidratos:
            print(carbohidratos[x])
    elif peso >= 70 and peso < 80:
        for x in proteinas:
            print(proteinas[x])
    elif peso >= 80:
        for x in fibras:
            print(fibras[x])
    
menus()