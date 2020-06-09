months = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

selection = 'Si'

while selection == 'Si':
    number = int(input('Ingresa un mes en número que deseas visualizar: '))

    if number < 1 or number > 12: 
        print("Ingresa un número válido")
        number = int(input('Ingresa un mes en número que deseas visualizar: '))
    
    else: 
        print(f'El mes que deseaste ver es: {months[number-1]}')

    selection = input('¿Deseas visualizar otro mes [Si/No]? ')