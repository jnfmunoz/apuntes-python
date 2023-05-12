class Ticket:

    def __init__(self, _precio, _fecha_venta, _numero_ticket, _tipo_ticket):
        self.precio = _precio
        self.fecha_venta = _fecha_venta
        self.numero_ticket = _numero_ticket
        self.tipo_ticket = self.tipos_ticket["normal"]

class Token:

    tipos_pago = {
        'efectivo':'efectivo',
        'credito':'credito',
        'debito':'debito'
    }

    def __init__(self, _tipo_papel, _cantidad_venta):
        self.tipo_pago = self.tipos_pagos["efectivo"]
        self.cantidad_venta = _cantidad_venta

class Atraccion:

    tipos_persona = {
        'niño':'niño',
        'adulto':'adulto'
    }
    
    def __init__(self, _capacidad, _nombre, _cantidad_uso):
        self.capacidad = _capacidad
        self.tipo_persona = self.tipos_persona["adulto"]
        self.nombre = _nombre
        self.cantidad_uso = _cantidad_uso
        # self.tipo_ticket = _tipo_ticket