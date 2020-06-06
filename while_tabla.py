print(''''
BIENVENIDO A LA TABLA DE MULTIPLICAR''')
'''
number = int(input('Introduce el número que quieras multiplicar hasta el 25: '))
selection = 'Si'
while selection == 'Si':
    for i in range(0, 26):
        print("La tabla de multiplicar {} * {} es de: {}:".format(i, number,  number*i))
    selection = input('Deseas calcular otro número (Si/No): ')
print("Hasta luego")
'''
selection = 'Si'

while selection == 'Si':
    number = int(input('Introduce un número: '))
    counter = 1

    while counter < 26:
        print (f'{number} x {counter} = {number * counter}')
        counter += 1
    selection = input('¿Deseas calcular otro número (Si/No): ')

print('Hasta luego')
