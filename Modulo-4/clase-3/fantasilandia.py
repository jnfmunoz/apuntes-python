class Ticket: 

    types = [
        {
            "type": "General",
            "price":5000,
            "correlation_number":0
        },
        {
            "type": "VIP",
            "price":10000,
            "correlation_number":0
        }
    ]

    def __init__(self, _sale_date ,_type):
        self.tipo_ticket = self.types[0]
        self.number = self.types[_type]["correlation_number"]+1
        self.types[_type]["correlation_number"]+=1

class Token:
    type_pappers = {
        "normal":1,
        "sellado":2,
    }

    type_pays = {
        "transbank": 1,
        "Paypal":2,
        "mercado_pago":3,
        "cash":4,
    }

    sales_quantity = 5

    def __init__(self):
        self.type_pappers = 0
        self.type_pay = 0

class Atraction:
    type_person = {
        "child":0,
        "mayor":1,
    }

    #Variables de clase
    use_quantity = 0

    def __init__(self, _type_person, _capacity, _name):
        #Variables de instancia
        self.type_person = self.type_person[_type_person]
        self.capacity = _capacity
        self.name = _name

ticket_one = Ticket()
ticket_two = Ticket()

token_one = Token()
token_two = Token()
token_three = Token()

carrousel = Atraction()
cars = Atraction()
sillas = Atraction()