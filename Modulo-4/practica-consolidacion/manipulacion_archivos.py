from clases import *
import csv

def guardar(file_name, Vehiculo):
    file = open(file_name, "a")
    datos = [(Vehiculo.__class__, Vehiculo.__dict__)]
    csv_file = csv.writer(file)
    csv_file.writerows(datos)
    file.close()

def recuperar(file_name):
    vehiculos = []
    file = open(file_name, "r")
    file_csv = csv.reader(file)
    for vehiculo in file_csv:
        vehiculos.append(vehiculo)
    file.close()
    return vehiculos

#automovil = Automovil("Ford", "Fiesta", 4, 180, 500)
particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

#guardar("vehiculos.csv", automovil)
guardar("vehiculos.csv", particular)
guardar("vehiculos.csv", carga)
guardar("vehiculos.csv", bicicleta)
guardar("vehiculos.csv", motocicleta)

vehiculos = recuperar("vehiculos.csv")
for x in vehiculos:
    print(x)

"""
'r' - reading mode. The default. It allows you only to read the file, not to modify it. 
When using this mode the file must exist.
'w' - writing mode. It will create a new file if it does not exist, otherwise will erase 
the file and allow you to write to it.
'a' - append mode. It will write data to the end of the file. It does not erase the file, 
and the file must exist for this mode.
'rb' - reading mode in binary. This is similar to r except that the reading is forced in 
binary mode. This is also a default choice.
'r+' - reading mode plus writing mode at the same time. This allows you to read and write 
into files at the same time without having to use r and w.
'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
'wb' - writing mode in binary. The same as w except the data is in binary.
'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, 
a new one is made. Otherwise, the file is overwritten.
'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
'ab' - appending in binary mode. Similar to a except that the data is in binary.
'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file 
does not exist. Otherwise, the file pointer is at the end of the file if it exists.
'ab+' - appending and reading mode in binary. The same as a+ except that the data is in 
binary.
"""