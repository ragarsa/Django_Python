cellphone = {
    'marca' : 'Xiaomi',
    'RAM' : 6,
    'almacenamiento': 64, 
    'color' : 'negro'
}

print(cellphone)

print(f"La marca es :",cellphone['marca'])

nue_marca = input('Dame el nombre de la nueva marca: ')

#Agregar un valor del diccionario
cellphone['marca'] = nue_marca

print(cellphone)

#Agregar un nuevo elemenot a un diccionario

so = input('¿Cuál es el sistema operativo? ')

cellphone['SO'] = so

print(cellphone)

#Eliminar un elemento de un diccionario
print('Eliminando color')

del cellphone['color']
print(cellphone)




#Iterando un diccionario se tienen dos valores 
# por cada iteración
print(cellphone.items())

for clave, valor in cellphone.items():
    print(f'La clave es {clave}, y su valor es {valor}')



#Iterando solo las claves

for clave in cellphone.keys():
    print(f"La clave es: {clave}")

#Iterando solo las valores

for valor in cellphone.values():
    print(f"El valor es {valor} ")
