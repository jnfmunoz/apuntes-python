'''trabajando con diccionarios'''

empty_dict = {}

fullfiled_dict = {
    "id": 1,
    "name": "Valeria"
}

print(empty_dict)
print(fullfiled_dict)

lista_1 = ['a1', 'b2']
dict_converted = dict(lista_1)
print(dict_converted)

tupla_1 = ('a1', 'b2')
print(tupla_1), dict(tupla_1)

list_dimensional = [['a1', 1], ['b', 2]]
print(list_dimensional), dict(list_dimensional)
