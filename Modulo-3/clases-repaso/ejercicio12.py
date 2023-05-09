def grupoCurso():
    nombre = input("Ingrese nombre: ")
    genero = input("Ingrese genero(M o F): ")
    curso = "None"

    if genero.lower() == "f":
        if nombre.lower() < "m":
            curso = "A"
        else:
            curso = "B"
    else:
        if nombre.lower() > "n":
            curso = "A"
        else:
            curso = "B"
    print('-----------------------------------')
    print(f"Tu grupo curso es: {curso}")

grupoCurso()