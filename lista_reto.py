lista = ['MX', 'US', 'UK', 'MX', 'MX', 'US', 'UK', 'FR', 'CH', 'CH']

lista.append('JP')

print("El elemento 'MX' se encuentra", lista.count('MX')," veces en la lista")

print("El index de donde aparece 'UK' por primera vez es en ", lista.index('UK'))

lista_2 = lista.copy()

lista_2.extend(['COL','ARG','BR'])
 
print(lista_2)

lista_2.remove('CH')
lista_2.remove('CH')

print(lista_2)
