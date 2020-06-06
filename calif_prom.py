selection = 'Si'


calif_list = []

name = input('Ingresa tu nombre completo: ')

while selection == 'Si':
    calif_mater = int(input('Ingresa la calificación de una materia: '))
    calif_list.append(calif_mater)
    selection = input('¿Deseas agregar otra calificación? ')

suma_calif = 0

for i  in calif_list:
    suma_calif += i

promedio = float(suma_calif / len(calif_list))

print(f'El promedio de {name} es {promedio}')
