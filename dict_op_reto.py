#1._ Vamos a recibir del teclado un país
# y la cantidad de personas que viven ahí en millones
#2. Construye un diccionario donde 
# cada país va a ser la clave
# y cantidad de personas el valor

#3.- El usuario podrá ingresar países
#Hasta que ya no quiera
#paises = {'USA': 50, 'MEXICO': 30}

#1.1 Imprime todos los paises dentro del diccionario
#con la cantidad de habitantes

#4.- Pide el usuario el nombre de un país,
#para poder ver la cantidad de personas

#5.- Accede al elemento del diccionario, 
#que contiene ese dato


selection = 'Si'

mundo = {}
while selection == 'Si':


    pais = str(input('Ingresa el nombre del país: '))
    habi = int(input('Ingresa el número de habitantes de ese país: '))

    
    
    mundo[pais] = habi


    selection = input('¿Deseas agregar otro país [Si/No]? ')

for clave, valor in mundo.items():

    print(f"El país {clave}, tiene {valor} millones de habitantes")


eleccion = str(input('¿Qué país deseas ver sus habitantes? '))


print(f"{eleccion} tiene {mundo[eleccion]} millones de personas")
