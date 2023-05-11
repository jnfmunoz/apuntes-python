requisitos = {
    "titulo": "requerido",
    "notas": "requerido",
    "foto": "opcional",
}

print(requisitos)

#acceder a una propiedad
print(f'las notas son de tipo: {requisitos["notas"]}')
print(f'la foto es de tipo {requisitos["foto"]}')

#modificar una propiedad
requisitos["foto"] = "requerido"
requisitos["titulo"] = "opcional"

print(f'la foto es de tipo {requisitos["foto"]}')
print(f'el titulo es de tipo {requisitos["titulo"]}')

avion = {
    "piloto":{
        "nombre": "Carlos",
        "apellido": "Azocar"
    },
    "cantidad_motores": 2,
    "operativo": True,
    "encendido": False,
    "activo": False,
    "do_escala":True,
    "is_flying": True,
    "seats": ['economic', 'turist', 'executive'],
    "capacidad_cargo": 1.7,
    "cantidad_pasajeros": 400,
    "modelo":"Boeing 747 MAX",
}