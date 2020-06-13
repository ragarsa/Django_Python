#El objetivo del programa es contar
#cuantas vees una palabra está contenido
#en el texto
#1. Separa el texto, guardando cada palabra como un elemento de una lsita
#2. Itera la lista y guarda cada palabra como un elemento de un diccionario,
#donde se valor va a ser la cantidad de veces que aparece esa palabra
texto = 'Este texto tiene algunas palabras Este otro texto con algunas palabras diferentes'

lst_palabras = texto.split(" ")
print(lst_palabras)

dic = {}

#PRIMERA SOLUCION
#for palabra in lst_palabras:
 #   dic[palabra] = lst_palabras.count(palabra)


for palabra in lst_palabras:
   if palabra not in dic:
      dic[palabra] = 1
    
   else: 
      dic[palabra] += 1

for palabra, contador in dic.items():
   print(f'Palabra: {palabra} aparece: {contador}')


        

#¿Cómo verificar si ya existe una clave en un diccionario?

#if clave in diccionario:
