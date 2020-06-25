class Person: 
    def __init__(self, name, last_name, age, gender):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        

    def get_name(self):
        return f'Mi nombre es {self.name} {self.last_name}'

    def get_gender(self):
        return f'El sexo de {self.name} es: {self.gender}'

    def birth(self):
        return f'Naciste en el año {self.age-2020}'

class Student(Person):

    def __init__(self, matricula, promedio, *args):
        super(Student, self).__init__(*args)
        self.matricula = matricula
        self.promedio = promedio
    
    def get_student_info(self):
        return f'El nombre del alumno es {self.get_name()} - Matricula {self.matricula}'


class Teacher(Person):

    def __init__(self, cedula, email, *args):
        super(Teacher, self).__init__(*args)
        self.cedula = cedula
        self.email = email
    
    def get_teacher_info(self):
        return f'{self.get_name()} - Cédula {self.cedula}'

student = Student(1232434, 9.5,'Raul', 'Sánchez', 28, 'M')
print(student.get_name())
print(student.get_student_info())

teacher = Teacher(8715645, 'tal@institucion.com', 'Martín', 'Rodriguez', 25, 'M')
teacher.get_name()
teacher.get_teacher_info()