class Cuenta:
    #titular, cantidad 
    def __init__(self, _titular):
        self.titular = _titular
        self.cantidad = 0

    def agregar_monto(self, _titular ,_monto):
        self.titular = _titular
        self.cantidad = self.cantidad + _monto

    def retirar_monto(self, _titular, _monto):
        self.titular = _titular
        self.cantidad = self.cantidad - _monto
    
    def mostrar_datos(self, _titular):
        if self.titular == _titular:
            print(f'nro cta: {self.titular}, monto cta: ${self.cantidad}')
    
titular1 = Cuenta(20045286)
titular2 = Cuenta(19382291)
titular3 = Cuenta(19111783)

titular1.agregar_monto(20045286, 50000)
titular1.agregar_monto(20045286, 80000)
titular2.agregar_monto(19382291, 20000)
titular2.agregar_monto(19382291, 81000)
titular3.agregar_monto(19111783, 30000)
titular3.agregar_monto(19111783, 75000)

titular1.retirar_monto(20045286, 20000)
titular1.retirar_monto(20045286, 10000)
titular2.retirar_monto(19382291, 500)
titular2.retirar_monto(19382291, 500)
titular3.retirar_monto(19111783, 3000)
titular3.retirar_monto(19111783, 2000)

titular1.mostrar_datos(20045286)
titular2.mostrar_datos(19382291)
titular3.mostrar_datos(19111783)