def cuentaAhorro():
    interes = 0.04
    dinero = int(input("Ingrese cantidad de dinero a ahorrar: "))
    saldo_anio_1 = round((dinero*interes)+dinero,2)
    saldo_anio_2 = round((saldo_anio_1*interes)+saldo_anio_1, 2)
    saldo_anio_3 = round((saldo_anio_2*interes)+saldo_anio_2, 2)

    print(f"Cantidad de ahorro proyectada al primer año ${saldo_anio_1}")
    print(f"Cantidad de ahorro proyectada al segundo año ${saldo_anio_2}")
    print(f"Cantidad de ahorro proyectada al tercer año ${saldo_anio_3}")

cuentaAhorro()