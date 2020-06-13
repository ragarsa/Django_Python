class Alumno:
    def __init__(self, matricula, name, surname, age, average, scholar_year):
        self.matricula = matricula
        self.name = name
        self.surname = surname
        self.age = age
        self.average = average
        self.scholar_year = scholar_year
    
    
    def get_matricula(self):
        return self.matricula
    
    def set_name(self, matricula):
        self.matricula = matricula 
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name 

    def get_surname(self):
        return self.surname
    
    def set_surname(self, surname):
        self.surname = surname
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age 

    def get_average(self):
        return self.average
    
    def set_average(self, average):
        self.average = average 

    def get_scholar_year(self):
        return self.scholar_year
    
    def set_scholar_year(self, scholar_year):
        self.scholar_year = scholar_year 

    def start_year(self):
        year = 2020-self.scholar_year
        print(f'El alumno ingresó en el año {year}')

    def start_age(self):
        start_age = self.age - self.scholar_year
        print(f'El alumno entró de {start_age} años')

    def get_print(self):
        print(f'Nombre: {self.name}. Matrícula: {self.matricula}. Promedio: {self.average}')


alumno = Alumno('ABC123', 'Raul', 'Sanchez', 28, 9.5, 5)

alumno.start_year()
alumno.start_age()

alumno.get_print()

alumno.set_average(9)

print(alumno.get_average())
