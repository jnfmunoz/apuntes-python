class Banco:
    cuentas = [] #guardar cuentas y correlativos
    movimientos = [] # guardar los movimientos
    #numero_movimientos = []

    def __init__(self):
        pass

    def agregar_cuenta(self, _cuenta, _rut):
        self.cuentas.append({
            'cuenta': _cuenta,
            'rut': _rut,
            'correlativo_movimiento': 0,
            'saldo': 0
        })
    
    def agregar_movimiento_for(self, _cuenta, _fecha, _tipo, _monto):
        for cuenta in self.cuentas:
            if cuenta['cuenta'] == _cuenta:
                if _tipo == 'Retiro':
                    if cuenta['saldo'] - _monto < 0:
                        print("saldo insuficiente")
                    else:
                        self.movimientos.append({
                            'cuenta': _cuenta,
                            'correlativo_movimiento': cuenta['correlativo_movimiento'],
                            'fecha': _fecha,
                            'tipo': _tipo,
                            'monto': _monto,
                            'saldo': cuenta['saldo'] - _monto
                        })
                        cuenta['saldo'] = cuenta['saldo'] - _monto
                        cuenta['correlativo_movimiento'] = cuenta['correlativo_movimiento'] + 1
                else:
                    self.movimientos.append({
                            'cuenta': _cuenta,
                            'correlativo_movimiento': cuenta['correlativo_movimiento'],
                            'fecha': _fecha,
                            'tipo': _tipo,
                            'monto': _monto,
                            'saldo': cuenta['saldo'] - _monto
                        })
                    cuenta['saldo'] = cuenta['saldo'] + _monto
                    cuenta['correlativo_movimiento'] = cuenta['correlativo_movimiento'] + 1
                break
    
    def estado_cuenta(self, _cuenta):
        print(self.movimientos)
        movimientos_cuenta = list(filter(lambda x :x['numero_cuenta'] == _cuenta, self.movimientos))
        print(movimientos_cuenta)
    
banco_bci = Banco()

banco_bci.agregar_cuenta('20045286', '20.045.286-0')
banco_bci.agregar_cuenta('20045287', '20.045.286-1')

print(Banco.cuentas)

print(banco_bci.agregar_movimiento_for("20045286", "17/04/2023", "Abono", 1000))
print(banco_bci.agregar_movimiento_for("20045286", "17/04/2023", "Abono", 10000))
print(banco_bci.agregar_movimiento_for("20045286", "17/04/2023", "Retiro", 3000))

