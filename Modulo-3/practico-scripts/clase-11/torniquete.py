class Torquinete:
    def __init__(self):
        self.tarifa = 730 #valor tarifa normal
        self.pasajes = [] #guardar todos los pagos de pasajes
     
    def pago_pasaje(self, _patente_vehiculo, _tipo_pasajero, _fecha):
        if _tipo_pasajero == "Hombre" or _tipo_pasajero == "Mujer":
            self.pasajes.append({
                'patente_vehiculo': _patente_vehiculo,
                'tipo_pasajero': _tipo_pasajero,
                'tarifa': self.tarifa,
                'fecha': _fecha,
                'correlativo_pasaje': 1,
            })
        elif _tipo_pasajero == "Adulto Mayor":
            self.pasajes.append({
                'patente_vehiculo': _patente_vehiculo,
                'tipo_pasajero': _tipo_pasajero,
                'tarifa': self.tarifa*0.5,
                'fecha': _fecha,
                'correlativo_pasaje':1,
            })
        elif _tipo_pasajero == "Niño":
            self.pasajes.append({
                'patente_vehiculo': _patente_vehiculo,
                'tipo_pasajero': _tipo_pasajero,
                'tarifa': 0,
                'fecha': _fecha,
                'correlativo_pasaje':1,
            })
    
micro = Torquinete()

micro.pago_pasaje("RR8266","Hombre", "02/05/2023")
micro.pago_pasaje("RR8266","Mujer", "02/05/2023")
micro.pago_pasaje("RR8266","Adulto Mayor", "02/05/2023")
micro.pago_pasaje("RR8266","Niño", "02/05/2023")
print(micro.pasajes)

