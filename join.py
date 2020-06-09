selection = 'Si'

names = []



while selection == 'Si':
    
	name = input('Ingresa el nombre de la persona: ')

	names.append(name.capitalize())

	selection = input('¿Deseas ingresar a otra persona [Si/No]? ')

print(','.join(names))

	