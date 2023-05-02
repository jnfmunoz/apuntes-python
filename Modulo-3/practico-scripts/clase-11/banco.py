class Banco:

    def __init__(self):
        self.cuentas = []#guardar las cuentas y correlativos
        self.movimientos = []

    def agregar_cuenta(self, _cuenta, _rut):
        self.cuentas.append({
            'numero_cuenta': _cuenta,
            'rut': _rut,
            'correlativo_movimiento':1,
            'saldo':0
        })
    def agregar_movimiento_for(self, _cuenta, _fecha, _tipo, _monto):
        for x in self.cuentas:
            if x['numero_cuenta'] == _cuenta:
                if _tipo == 'Retiro':
                    if x['saldo'] - _monto < 0:
                        print("saldo insuficiente")
                    else:
                        self.movimientos.append({
                            'numero_cuenta': _cuenta,
                            'correlativo_movimiento': x['correlativo_movimiento'],
                            'fecha': _fecha,
                            'tipo': _tipo,
                            'monto': _monto,
                            'saldo': x['saldo'] - _monto
                        })
                        x['saldo'] = x['saldo']-_monto
                        x['correlativo_movimiento'] = x['correlativo_movimiento'] +1
                else:
                    self.movimientos.append({
                            'numero_cuenta': _cuenta,
                            'correlativo_movimiento': x['correlativo_movimiento'],
                            'fecha': _fecha,
                            'tipo': _tipo,
                            'monto': _monto,
                            'saldo': x['saldo'] + _monto
                        })
                    x['saldo'] = x['saldo'] + _monto
                    x['correlativo_movimiento'] = x['correlativo_movimiento'] + 1
                break
    def estado_cuenta(self, _cuenta):
        movimientos_cuenta = list(filter(lambda x:x['numero_cuenta'] == _cuenta, self.movimientos))
        print("{:<20}".format(" Nº Mvto."),  "{:<20}".format("Fecha"),   "{:<20}".format("Tipo"),   "{:<20}".format("Monto"),  "{:<20}".format("Saldo"))
        for x in movimientos_cuenta:
            print("{:<20}".format(x['correlativo_movimiento']),  "{:<20}".format(x['fecha']),   "{:<20}".format(x['tipo']),   "{:<20}".format(x['monto']),  "{:<20}".format(x['saldo']))

banco_bci = Banco()

banco_bci.agregar_cuenta("840001", "20.045.286-0")
banco_bci.agregar_cuenta("840002", "19.382.291-6")

banco_bci.agregar_movimiento_for("840001", "17/04/2023", "Abono", 1000)
banco_bci.agregar_movimiento_for("840001", "17/04/2023", "Abono", 500)
banco_bci.agregar_movimiento_for("840001", "17/04/2023", "Retiro", 100)
banco_bci.agregar_movimiento_for("840001", "17/04/2023", "Abono", 1000)
banco_bci.agregar_movimiento_for("840001", "17/04/2023", "Retiro", 500)

banco_bci.agregar_movimiento_for("840002", "17/04/2023", "Abono", 3000)
banco_bci.agregar_movimiento_for("840002", "17/04/2023", "Abono", 100)
banco_bci.agregar_movimiento_for("840002", "17/04/2023", "Retiro", 750)

#Listar todas las cuentas
#print(banco_bci.cuentas)
#print(banco_bci.agregar_movimiento_for)
banco_bci.estado_cuenta("840001")
banco_bci.estado_cuenta("840002")
