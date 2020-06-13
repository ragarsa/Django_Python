class Person:
    def __init__(self, name, surname, age, height, weight):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
    
    def get_name(self):
        print(f'El nombre completo es: {self.name} {self.surname}')

    def indice_masa (self):
        imc= (self.weight / (self.height ** 2))

        print(f'El índe de masa corporal de {self.name} {self.surname} es: {imc:.3f}')

name = input('Ingresa tu nombre: ')

surname = input('Ingresa tu apellido: ')

age = int(input('Ingresa tu edad: '))

height = float(input('Ingresa tu altura: '))

weight = float(input('Ingresa tu peso: '))

person = Person(name, surname, age , height, weight)

person.get_name()

person.indice_masa()