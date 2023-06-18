from clases import Vehiculo, Particular, Carga, Bicicleta, Motocicleta

#automovil = Automovil("Ford", "Fiesta", "4", "180", "500")
particular = Particular("Ford", "Fiesta", "4", "180", "500", "5")
carga = Carga("Daft Trucks", "G 38", "10", "120", "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

#guardar("vehiculos.csv", automovil)
Vehiculo.guardar("vehiculos.csv", particular)
Vehiculo.guardar("vehiculos.csv", carga)
Vehiculo.guardar("vehiculos.csv", bicicleta)
Vehiculo.guardar("vehiculos.csv", motocicleta)

vehiculos = Vehiculo.recuperar("vehiculos.csv")
Vehiculo.imprimir_por_clase(vehiculos)