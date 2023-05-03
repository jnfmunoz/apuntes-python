class Transporte:
    def __init__(self) -> None:
        self.patentes = []
        self.movimientos = []
        self.tarifa = 730
        self.tarifario = {
            'adulto': self.tarifa,
            'niño':0,
            'adulto mayor': self.tarifa/2
        }

    def registrar_patente(self, _patente, _chofer):
        patente = list(filter(lambda x: x['patente'] == _patente, self.patentes))
        
        if len(patente) > 0:
            print("La patente ya se encuentra registrada")            
        else:
            self.patentes.append({
                "patente": _patente,
                "chofer": _chofer,
            })
            
    def cobrar_pasaje(self, _patente, _tipo_persona, _fecha):
        self.movimientos.append({
            "patente": _patente,
            "tipo_persona": _tipo_persona,
            "fecha": _fecha,
            "monto_cobrado": self.tarifario[_tipo_persona],
        })

    def reporte_diario(self, _tipo_reporte, _valor):
        movimientos = list(filter(lambda x: x[_tipo_reporte]== _valor, self.movimientos))
        total_cobrado = 0
        for pasaje in movimientos:
            total_cobrado += pasaje['monto_cobrado']
            print(pasaje['fecha'], pasaje['tipo_persona'], pasaje['monto_cobrado'])
        
        print("----------------")
        print(f'total cobrado es: {total_cobrado}')
        print("----------------")

empresa = Transporte()

empresa.registrar_patente("RR8266", "Rodrigo")

empresa.cobrar_pasaje("RR8266", "adulto", "02-05-2023")
empresa.cobrar_pasaje("RR8266", "adulto mayor", "02-05-2023")
empresa.cobrar_pasaje("RR8266", "adulto", "02-05-2023")

empresa.reporte_diario("tipo_persona", "adulto mayor")
empresa.reporte_diario("tipo_persona", "adulto")