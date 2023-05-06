def calculoHoras():
    horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
    coste_horas = float(input("Ingrese el valor coste por hora: "))

    pago = horas_trabajadas * coste_horas

    print(f"El pago que corresponde es de ${pago} pesos")

calculoHoras()