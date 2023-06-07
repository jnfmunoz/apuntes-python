numbers = [3, 87, 40, 65, 100, 40,1000, 4, 0, 2, 40, 40]

encontrados = []
for maravilla in numbers:
    if maravilla == 40:
        encontrados.append(maravilla)

print(encontrados)


encontrados_dos = list(filter(lambda x: x == 40, numbers))

print(encontrados_dos)


