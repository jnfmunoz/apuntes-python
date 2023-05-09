def pizzeria():
    tipoPizza = input("pizza vegetariana? s/n: ")
    veggie = ['Pimiento', 'Tofu']
    normal = ['Pepperoni', 'Jamón', 'Salmón']
    descripcion = "None"

    if tipoPizza.lower() == "s":
        descripcion = "Pizza Vegetariana"
        print("-------------------------------------")
        print(f"Tipo pizza: {descripcion}")
        print("-------------------------------------")
        print("Ingredientes disponibles")
        for x in veggie: 
            print(x)

    else: 
        descripcion = "Pizza Normal"
        print("-------------------------------------")
        print(f"Tipo pizza: {descripcion}")
        print("-------------------------------------")
        print("Ingredientes disponibles")
        for x in normal: 
            print(x)
    
    ingrediente = input("Seleccione un ingrediente: ")
    print("-------------------------------------")
    print("Detalle pizza")
    print(f"{descripcion} con ingredientes base de mozzarella y tomate")
    print(f"Ingrediente adicional: {ingrediente}")

pizzeria()