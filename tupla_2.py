nombres = input('Dame los nombres que quieras introducir: ')

lista_nombres = nombres.split(",")

tupla_nombres = tuple(lista_nombres)

print("La cantidad de nombres es:", len(tupla_nombres))


print("El valor máximo de la tupla es:", max(tupla_nombres))

print("El valor mínimo de la tupla es:", min(tupla_nombres))
