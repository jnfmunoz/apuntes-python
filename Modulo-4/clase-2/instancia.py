class Taza:
    sizes = {
        "small": "pequeño",
        "medium": "mediano",
        "large": "largo",
    }

    def __init__(self):
        self.size = self.sizes["small"]


class Maquina:
    
    def __init__(self, _tipo_cafe ,_cantidad_agua, _cantidad_cafe):
        self.tipo_cafe = self._tipo_cafe
        self.cantidad_agua = self._cantidad_agua
        self.cantidad_cafe = self._cantidad_cafe

class Cafe:
    coffee_types = {
        "arabic": "arabico",
        "robust": "robusto",
    }

    def __init__(self):
        self.type = self.coffee_types["arabic"]

class Leche:
    milk_types = {
    'skimmed':'semidescremada',
    'skim':'descremada',
    'lactose_free':'deslactosada',
    'soy':'soya',
    'almond':'almendra',
    }

    def __init__(self):
        self.milk_types = self.milk_types["skimmed"]