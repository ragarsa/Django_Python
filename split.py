text = "Martin_8/9$Juan_5/4/9/8$Francisco_10/10/10/9"
students_list = text.split("$")
print(students_list)
tup = tuple(students_list)
print(tup)
for student in students_list:
    values = student.split("_")
    print(values)

    name = values[0]
    print('Nombre',name)

    califs = values[1].split('/')
    print('Calificaciones', califs)

    suma = 0

    for calif in califs:
        suma += float(calif)
    print (suma)
    avg = suma / len(califs)
    print(f'La calificación final de {name} es: {avg}')