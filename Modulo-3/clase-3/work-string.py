'''Strings'''

first_name = "Richard"
last_name = "Lujano"

#concatenacion
print(first_name + " " + last_name)

#multiplicacion
mensaje1= "Hola "*3
print(mensaje1)

#Añadir
mensaje3 = "Francisco"
print(mensaje3)
mensaje3 += ","
print(mensaje3)
mensaje3 += "Muñoz"
print(mensaje3)

#Funcion built in: Len
print(len(mensaje3))

#owl function : find, busca la coincidencia dentro de una cadena
cadena = "esto es una cadena de texto"

posicion = cadena.find("pelo")
print("pelo se encuentra en:", posicion);
posicion = cadena.find("cadena")
print("cadena se encuentra en:", posicion)

#String replace
name = "Homero Simpson"
new_name = name.replace("Homero", "Bart")
print(name , "|", new_name)

'''Listas'''
#Lista vacía de la forma más óptima
empty_list = []
print(empty_list)

fullfiled_list = [1,3,500,1.4, [2,"a"], {"name":"Juan"}, (1,3,5)]
print(fullfiled_list)

#list(), crear una lista vacía, permite convertir a lista
second_list = list()
print(second_list)

print(list("Concurso"))

range_one = range(10)
print(list(range_one))

#Operaciones
#Agregar item a la lista
third_list = ["a","b"]
print(third_list)
third_list.append("c")
print(third_list)

#Seleccionar o extraer un item de la lista: con la posición -> lista[posicion]


#Iterar una lista
print ("Recorrer lista por Indices")
for x in range(0,len(third_list)):
    print (third_list[x])

#Eliminar un elemento de la lista
third_list.pop(2)
print(third_list)

#Modificar la lista
quarter_list = ['Pedro', 'Juan', 'Diego']
print(quarter_list)
quarter_list[1] = 'Romualdito'
print(quarter_list)

'''Tuplas'''
#Tuplas - inmutables
empty_tuple = ()
fullfiled_tuple = (1, "Juan", 518.677)

print(empty_tuple, "|" ,fullfiled_tuple)

one_tuple = ('Juan')
print(type(one_tuple))

hojas = 'carta', 'oficio'
print(type(hojas))
print(hojas)

empty_tuple_2 = tuple()

#Convertor o crear con function tuple()
list_to_convert = [2, 6, 8, 9]
print(list_to_convert)

tuple_converted = tuple(list_to_convert)
print(tuple_converted)

#reverse
tuple_to_reverse = (2,4,6,8,10,12,14)
print(tuple_to_reverse)
tuple_reversed = tuple(reversed(tuple_to_reverse))
print(tuple_reversed)

#append
tuple_to_append = ['Juan', 'Francisco' ,'Muñoz']
print(tuple_to_append)
tuple_to_append.append('Grau')
print(tuple_to_append)

#extend

#remove

#clear

#sort
list_to_sort = (5,2,4,2)
print(list_to_sort)
list_sorted = tuple(sorted(list_to_sort))
print(list_sorted)
