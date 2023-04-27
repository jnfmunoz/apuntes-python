words = "Esto es una cademna de texto "

word = ''
for letter in words:
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ''
print("\n------------- \n")
for letter in words:
    if letter != ' ':
        print(letter)
    else:
        break

print("\n---------------------\n")
animals_list = ['Gato', 'Perro', 'Pajaro', 'Ardilla']
for animal in animals_list:
    print(animal)

print("\n---------------------\n")

list1 = range(2,3) #[0,1,2,3]
print(list1)
for number_in in range(1, 10):
    print(number_in)

print("\n---------------------\n")

list1 = range(2,3) #[0,1,2,3]
print(list1)
for number_in in range(1, 10, 2):
    print(number_in)

print("\n---------- Tablas de Multiplicar -----------\n")
for num_tabla in range(1, 11):
    for num_mul in range(1, 10):
        result = num_tabla * num_mul
        print(f'{num_tabla} x {num_mul} = {result}')
    print("\n---------------------\n")


print("\n---------- Arreglos bidimencionales -----------\n")
double_list = [[1, 2, 3],[4, 6, 7]]

print(double_list[0])
print(double_list[1])

print(double_list[0][2])
print(double_list[1][1])