def evaluacion():
    nivel="None"
    cantidad=0
    base=2400

    hayMasDatos = "Si"
    while hayMasDatos == "Si":
        puntaje = float(input("Ingrese puntaje empleado: "))
        if puntaje in (0.1, 0.2, 0.3, 0.5):
            print("Puntaje invalido")
        else:
            if puntaje == 0.0:
                nivel = "Inaceptable"
                cantidad=0
            elif puntaje == 0.4:
                nivel="Aceptable"
                cantidad=puntaje*base
            elif puntaje >= 0.6:
                nivel="Meritorio"
                cantidad=puntaje*base
            print(f"Nivel empleado {nivel}")
            print(f"Cantidad de dinero a cobrar: ${cantidad}")
            hayMasDatos = input("Desea continuar? <Si-No>: ")
            
evaluacion()